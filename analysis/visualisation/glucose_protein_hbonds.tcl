# VMD: display ONLY glucose-protein hydrogen bonds, updating with the frame.
#
# 1. Hide (do not delete) your existing HBonds representation(s).
#    Leave your protein/cartoon and glucose/stick representations visible.
# 2. Load this file in Extensions > Tk Console:
#       source /full/path/to/glucose_protein_hbonds.tcl
#    Or open a file chooser:
#       source [tk_getOpenFile]
#
# The script starts automatically on the TOP molecule. It copies the distance
# and angle cutoffs from the FIRST existing HBonds representation (hidden or
# visible). With no such representation, it uses 3.0 Angstrom / 20 degrees.
# The angle is deviation from a straight (180-degree) D-H-A arrangement.
#
# Commands after loading:
#   glc_hbonds                 Restart, copying existing HBonds cutoffs.
#   glc_hbonds 3.5 30          Restart with explicit cutoffs (example only).
#   glc_hbonds 3.5 30 0        Use molecule ID 0 instead of the top molecule.
#   glc_hbonds_off             Remove these lines and stop automatic updates.
#
# Requirements: protein and glucose must be in the same loaded VMD molecule,
# with explicit hydrogens and correct covalent connectivity. Glucose residue
# names must be AGLC and/or BGLC. This is a geometric visualization, not an
# independent chemical validation or an analysis of H-bond occupancies.
# Uses the loaded coordinates; does not reimage periodic neighbours. Keep the
# protein whole and position neighbouring glucose molecules around it first.
# Does not change coordinates, topology, representations, or trajectory files.
# Only graphics objects created by this script are removed on refresh/stop.
# Reload this script after loading a saved VMD session to resume the callback.
#
# Official API references:
# https://www.ks.uiuc.edu/Research/vmd/current/ug/node138.html
# https://www.ks.uiuc.edu/Research/vmd/current/ug/node129.html
# https://www.ks.uiuc.edu/Research/vmd/current/ug/node142.html

# Clean up an earlier copy before redefining the procedures.
if {[llength [info commands ::glc_hbonds_off]]} { ::glc_hbonds_off }

namespace eval ::GlcProteinHB {
    variable molid -1
    variable distance 3.0
    variable angle 20.0
    variable width 2
    variable graphics_ids {}
}

proc ::GlcProteinHB::clear {} {
    variable molid
    variable graphics_ids
    foreach id $graphics_ids { catch {graphics $molid delete $id} }
    set graphics_ids {}
}

proc ::glc_hbonds_off {} {
    variable ::GlcProteinHB::molid
    if {$molid >= 0} {
        catch {trace remove variable ::vmd_frame($molid) write ::GlcProteinHB::changed}
        ::GlcProteinHB::clear
    }
    set molid -1
    return
}

proc ::GlcProteinHB::redraw {} {
    variable molid
    variable distance
    variable angle
    variable width
    variable graphics_ids

    if {[lsearch -exact [molinfo list] $molid] < 0} {
        error "The selected molecule is no longer loaded."
    }
    ::GlcProteinHB::clear
    set frame [molinfo $molid get frame]
    # At least the original 4-Angstrom neighbourhood. If a larger H-bond
    # cutoff is explicitly used, enlarge the search shell to avoid omissions.
    set shell [expr {max(4.0, double($distance))}]
    set p ""
    set g ""
    set status [catch {
        set p [atomselect $molid {protein} frame $frame]
        set g [atomselect $molid \
            "resname AGLC BGLC and (same residue as (within $shell of protein))" \
            frame $frame]

        if {[$g num] > 0} {
            # Atom indices in measure hbonds are GLOBAL molecule indices.
            # Map them explicitly rather than treating them as selection indices.
            array set xyz {}
            foreach sel [list $p $g] {
                foreach idx [$sel get index] coord [$sel get {x y z}] {
                    set xyz($idx) $coord
                }
            }
            array set seen {}
            # Both directions: protein donates to glucose AND glucose to protein.
            foreach pair [list [list $p $g] [list $g $p]] {
                lassign $pair donors acceptors
                lassign [measure hbonds $distance $angle $donors $acceptors] ds as hs
                foreach d $ds a $as {
                    # Several hydrogens can give the same donor-acceptor line.
                    set key [lsort -integer [list $d $a]]
                    if {[info exists seen($key)]} { continue }
                    set seen($key) 1
                    lappend graphics_ids [graphics $molid line \
                        $xyz($d) $xyz($a) width $width style dashed]
                }
            }
        }
    } message options]
    if {$p ne ""} { catch {$p delete} }
    if {$g ne ""} { catch {$g delete} }
    if {$status} { return -options $options $message }
    return [llength $graphics_ids]
}

proc ::GlcProteinHB::changed {name index operation} {
    if {[catch {::GlcProteinHB::redraw} message]} {
        ::glc_hbonds_off
        puts "Glucose-protein H-bond drawing stopped: $message"
    }
}

proc ::glc_hbonds {{dist auto} {ang auto} {molecule top}} {
    variable ::GlcProteinHB::molid
    variable ::GlcProteinHB::distance
    variable ::GlcProteinHB::angle

    if {$molecule eq "top"} { set molecule [molinfo top] }
    if {[lsearch -exact [molinfo list] $molecule] < 0} {
        error "Load the protein/glucose structure and trajectory first."
    }
    if {[molinfo $molecule get numframes] < 1} {
        error "This molecule has no coordinate frames."
    }
    foreach text [list {protein} {resname AGLC BGLC}] {
        set test [atomselect $molecule $text]
        set count [$test num]
        $test delete
        if {$count == 0} { error "No atoms match '$text' in molecule $molecule." }
    }

    set old_dist 3.0
    set old_ang 20.0
    set source "fallback defaults"
    for {set i 0} {$i < [molinfo $molecule get numreps]} {incr i} {
        set rep [lindex [molinfo $molecule get [list "rep $i"]] 0]
        if {[string equal -nocase [lindex $rep 0] "HBonds"]} {
            set old_dist [lindex $rep 1]
            set old_ang [lindex $rep 2]
            set source "HBonds representation $i"
            break
        }
    }
    if {$dist eq "auto"} { set dist $old_dist } else { set source "explicit settings" }
    if {$ang eq "auto"} { set ang $old_ang } else { set source "explicit settings" }
    if {![string is double -strict $dist] || ![string is double -strict $ang]} {
        error "Use numerical distance/angle cutoffs, or auto."
    }
    if {$dist <= 0 || $ang <= 0 || $ang >= 180} {
        error "Distance must be positive; angle deviation must be between 0 and 180."
    }

    ::glc_hbonds_off
    set molid $molecule
    set distance $dist
    set angle $ang
    if {[catch {::GlcProteinHB::redraw} count options]} {
        ::glc_hbonds_off
        return -options $options $count
    }
    trace add variable ::vmd_frame($molid) write ::GlcProteinHB::changed
    puts "Glucose-protein H-bonds: molecule $molid; distance $distance A; angle deviation $angle degrees ($source)."
    puts "Current frame: $count distinct donor-acceptor lines. Updates follow the trajectory."
    puts "Keep old HBonds representations hidden. To stop: glc_hbonds_off"
    return
}

::glc_hbonds

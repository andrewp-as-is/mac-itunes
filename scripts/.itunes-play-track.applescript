#!/usr/bin/osascript


-- track        name/integer
-- playlist     name

on run argv
    set _track to (item 1 of argv)
    try
        set _track to _track as number
    end try
    set _playlist to (item 2 of argv)
    tell application "itunes" to play track _track of playlist _playlist
end run

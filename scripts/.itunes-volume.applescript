#!/usr/bin/osascript

-- volume.applescript [volume]

on run argv
    if count of argv is 1 then
        tell application "itunes" to set sound volume to (item 1 of argv)
    end if
    tell application "itunes" to sound volume
end run

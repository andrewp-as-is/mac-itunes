#!/usr/bin/osascript

tell application "itunes"
    if ((get player state as text) is "playing") then
        tell application "itunes" to pause
    end if
end tell

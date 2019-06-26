#!/usr/bin/osascript

tell application "iTunes"
  if get mute then
    return 1
  else
    return 0
  end if
end tell

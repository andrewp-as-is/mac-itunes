#!/usr/bin/osascript

on run argv
    tell application "itunes" to play playlist (item 1 argv as text)
end run

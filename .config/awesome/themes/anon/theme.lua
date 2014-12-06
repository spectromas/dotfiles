-- anon, awesome3 theme

--{{{ Main
local awful = require("awful")
awful.util = require("awful.util")

theme = {}

home          = os.getenv("HOME")
config        = awful.util.getdir("config")
shared        = "/usr/share/awesome"
if not awful.util.file_readable(shared .. "/icons/awesome16.png") then
    shared    = "/usr/share/local/awesome"
end
sharedicons   = shared .. "/icons"
sharedthemes  = shared .. "/themes"
themes        = config .. "/themes"
themename     = "/anon"
if not awful.util.file_readable(themes .. themename .. "/theme.lua") then
       themes = sharedthemes
end
themedir      = themes .. themename

wallpaper1    = themedir .. "/background.jpg"
wallpaper2    = themedir .. "/background.png"
wallpaper3    = sharedthemes .. "/zenburn/zenburn-background.png"
wallpaper4    = sharedthemes .. "/default/background.png"
wpscript      = home .. "/.wallpaper"

theme.useless_gap_width =19

--if awful.util.file_readable(wallpaper1) then
--  theme.wallpaper = wallpaper1
--elseif awful.util.file_readable(wallpaper2) then
--  theme.wallpaper = wallpaper2
--elseif awful.util.file_readable(wpscript) then
--  theme.wallpaper_cmd = { "sh " .. wpscript }
--elseif awful.util.file_readable(wallpaper3) then
--  theme.wallpaper = wallpaper3
--else
--  theme.wallpaper = wallpaper4
--end
--}}}
theme.font          = "Termsyn 8"

--COLOR_TITLE_FG='#c0c0dd'
--theme.bg_normal     = "#252525"
theme.bg_normal     = "#000000"
theme.bg_focus      = "#000000"
--theme.bg_focus      = "#252525"
theme.bg_urgent     = "#ff0000"

theme.fg_normal     = "#aaaaaa"
theme.fg_focus      = "#ffffff"
theme.fg_urgent     = "#ffffff"

theme.border_width  = 1
theme.border_normal = "#252525"
theme.border_focus  = "#aaaaaa"
theme.border_marked = "#91231c"

-- Display the taglist squares
theme.taglist_squares = false

-- You can add as many variables as
-- you wish and access them by using
-- beautiful.variable in your rc.lua
--bg_widget    = #cc0000

-- Display close button inside titlebar
theme.titlebar_close_button = true

-- {{{ Taglist
theme.taglist_squares_sel   = themedir .. "/taglist/squarefz.png"
theme.taglist_squares_unsel = themedir .. "/taglist/squareza.png"
--theme.taglist_squares_resize = "false"
-- }}}

return theme


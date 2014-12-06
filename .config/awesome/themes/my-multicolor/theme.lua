-- zenburn-custom, awesome3 theme, by Adrian C. (anrxc)

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
themename     = "/my-multicolor"
if not awful.util.file_readable(themes .. themename .. "/theme.lua") then
       themes = sharedthemes
end
themedir      = themes .. themename

wallpaper1    = themedir .. "/background.png"
wallpaper2    = themedir .. "/background.png"
wallpaper3    = sharedthemes .. "/zenburn/zenburn-background.png"
wallpaper4    = sharedthemes .. "/default/background.png"
wpscript      = home .. "/.wallpaper"

if awful.util.file_readable(wallpaper1) then
	theme.wallpaper = wallpaper1
elseif awful.util.file_readable(wallpaper2) then
	theme.wallpaper = wallpaper2
elseif awful.util.file_readable(wpscript) then
	theme.wallpaper_cmd = { "sh " .. wpscript }
elseif awful.util.file_readable(wallpaper3) then
	theme.wallpaper = wallpaper3
else
	theme.wallpaper = wallpaper4
end

if awful.util.file_readable("/vain/init.lua") then
    theme.useless_gap_width  = "10"
end
--}}}

-- {{{ Styles
--theme.font
--theme.font          = "bauhaus 8"
theme.font          = "terminus 8"


-- {{{ Colors
theme.menu_bg_normal = "#000000"
theme.menu_bg_focus = "#000000"
theme.bg_normal = "#000000"
theme.bg_focus = "#000000"
theme.bg_urgent = "#000000"
theme.fg_normal = "#aaaaaa"
theme.fg_focus = "#ff8c00"
theme.fg_urgent = "#af1d18"
theme.fg_minimize = "#ffffff"
theme.fg_black = "#424242"
theme.fg_red = "#ce5666"
theme.fg_green = "#80a673"
theme.fg_yellow = "#ffaf5f"
theme.fg_blue = "#7788af"
theme.fg_magenta = "#94738c"
theme.fg_cyan = "#778baf"
theme.fg_white = "#aaaaaa"
theme.fg_blu = "#8ebdde"
theme.border_width = "1"
theme.border_normal = "#1c2022"
theme.border_focus = "#606060"
theme.border_marked = "#3ca4d8"
theme.menu_width = "130"
theme.menu_border_width = "5"
theme.menu_fg_normal = "#aaaaaa"
theme.menu_fg_focus = "#ff8c00"
theme.menu_bg_normal = "#050505dd"
theme.menu_bg_focus = "#050505dd"
-- }}}

-- {{{ Titlebars
theme.titlebar_bg_focus  = "#3F3F3F"
theme.titlebar_bg_normal = "#3F3F3F"
-- theme.titlebar_[normal|focus]
-- }}}

-- {{{ Widgets
theme.fg_widget        = "#AECF96"
theme.fg_center_widget = "#88A175"
theme.fg_end_widget    = "#FF5656"
theme.fg_off_widget    = "#494B4F"
theme.fg_netup_widget  = "#7F9F7F"
theme.fg_netdn_widget  = "#CC9393"
theme.bg_widget        = "#3F3F3F"
theme.border_widget    = "#3F3F3F"
-- }}}

-- {{{ Mouse finder
theme.mouse_finder_color = "#CC9393"
-- theme.mouse_finder_[timeout|animate_timeout|radius|factor]
-- }}}

-- {{{ Tooltips
-- theme.tooltip_[font|opacity|fg_color|bg_color|border_width|border_color]
-- }}}

-- {{{ Taglist and Tasklist
-- theme.[taglist|tasklist]_[bg|fg]_[focus|urgent]
-- }}}

-- {{{ Menu
-- theme.menu_[bg|fg]_[normal|focus]
-- theme.menu_[height|width|border_color|border_width]
-- }}}
-- }}}


-- {{{ Icons
--
-- {{{ Taglist icons
theme.taglist_squares_sel   = themedir .. "/taglist/squarefz.png"
theme.taglist_squares_unsel = themedir .. "/taglist/squareza.png"
--theme.taglist_squares_resize = "false"
-- }}}

-- {{{ Misc icons
--theme.awesome_icon           = themedir .. "/awesome.png"
--theme.menu_submenu_icon      = sharedthemes .. "/default/submenu.png"
--theme.tasklist_floating_icon = sharedthemes .. "/default/tasklist/floatingw.png"
-- }}}

-- {{{ Layout icons
theme.layout_tile       = themedir .. "/icons/tile.png"
theme.layout_tileleft   = themedir .. "/icons/tileleft.png"
theme.layout_tilebottom = themedir .. "/icons/tilebottom.png"
theme.layout_tiletop    = themedir .. "/icons/tiletop.png"
theme.layout_fairv      = themedir .. "/icons/fairv.png"
theme.layout_fairh      = themedir .. "/icons/fairh.png"
theme.layout_spiral     = themedir .. "/icons/spiral.png"
theme.layout_dwindle    = themedir .. "/icons/dwindle.png"
theme.layout_max        = themedir .. "/icons/max.png"
theme.layout_fullscreen = themedir .. "/icons/fullscreen.png"
theme.layout_magnifier  = themedir .. "/icons/magnifier.png"
theme.layout_floating   = themedir .. "/icons/floating.png"
-- }}}

theme.awesome_icon = "/home/alex/.config/awesome/manjaro.png"

-- {{{ Widget icons
theme.menu_submenu_icon = "/home/alex/.config/awesome/themes/multicolor/icons/submenu.png"
theme.widget_temp = "/home/alex/.config/awesome/themes/multicolor/icons/temp.png"
theme.widget_uptime = "/home/alex/.config/awesome/themes/multicolor/icons/ac.png"
theme.widget_cpu = "/home/alex/.config/awesome/themes/multicolor/icons/cpu.png"
theme.widget_weather = "/home/alex/.config/awesome/themes/multicolor/icons/dish.png"
theme.widget_fs = "/home/alex/.config/awesome/themes/multicolor/icons/fs.png"
theme.widget_mem = "/home/alex/.config/awesome/themes/multicolor/icons/mem.png"
theme.widget_fs = "/home/alex/.config/awesome/themes/multicolor/icons/fs.png"
theme.widget_note = "/home/alex/.config/awesome/themes/multicolor/icons/note.png"
theme.widget_note_on = "/home/alex/.config/awesome/themes/multicolor/icons/note_on.png"
theme.widget_netdown = "/home/alex/.config/awesome/themes/multicolor/icons/net_down.png"
theme.widget_netup = "/home/alex/.config/awesome/themes/multicolor/icons/net_up.png"
theme.widget_mail = "/home/alex/.config/awesome/themes/multicolor/icons/mail.png"
theme.widget_batt = "/home/alex/.config/awesome/themes/multicolor/icons/bat.png"
theme.widget_clock = "/home/alex/.config/awesome/themes/multicolor/icons/clock.png"
theme.widget_vol = "/home/alex/.config/awesome/themes/multicolor/icons/spkr.png"
theme.widget_mpdplay = "/home/alex/.config/awesome/themes/multicolor/icons/note_on.png"
-- }}}


-- {{{ Titlebar icons
theme.titlebar_close_button_focus  = themedir .. "/titlebar/close_focus.png"
theme.titlebar_close_button_normal = themedir .. "/titlebar/close_normal.png"

theme.titlebar_ontop_button_focus_active    = themedir .. "/titlebar/ontop_focus_active.png"
theme.titlebar_ontop_button_normal_active   = themedir .. "/titlebar/ontop_normal_active.png"
theme.titlebar_ontop_button_focus_inactive  = themedir .. "/titlebar/ontop_focus_inactive.png"
theme.titlebar_ontop_button_normal_inactive = themedir .. "/titlebar/ontop_normal_inactive.png"

theme.titlebar_sticky_button_focus_active    = themedir .. "/titlebar/sticky_focus_active.png"
theme.titlebar_sticky_button_normal_active   = themedir .. "/titlebar/sticky_normal_active.png"
theme.titlebar_sticky_button_focus_inactive  = themedir .. "/titlebar/sticky_focus_inactive.png"
theme.titlebar_sticky_button_normal_inactive = themedir .. "/titlebar/sticky_normal_inactive.png"

theme.titlebar_floating_button_focus_active    = themedir .. "/titlebar/floating_focus_active.png"
theme.titlebar_floating_button_normal_active   = themedir .. "/titlebar/floating_normal_active.png"
theme.titlebar_floating_button_focus_inactive  = themedir .. "/titlebar/floating_focus_inactive.png"
theme.titlebar_floating_button_normal_inactive = themedir .. "/titlebar/floating_normal_inactive.png"

theme.titlebar_maximized_button_focus_active    = themedir .. "/titlebar/maximized_focus_active.png"
theme.titlebar_maximized_button_normal_active   = themedir .. "/titlebar/maximized_normal_active.png"
theme.titlebar_maximized_button_focus_inactive  = themedir .. "/titlebar/maximized_focus_inactive.png"
theme.titlebar_maximized_button_normal_inactive = themedir .. "/titlebar/maximized_normal_inactive.png"
-- }}}
-- }}}

return theme

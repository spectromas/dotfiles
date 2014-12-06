#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

# This file was automatically generated by calibre, do not edit it unless you know what you are doing.


#: Specify columns by which to sort the booklist on startup
# ID: sort_columns_at_startup
# Provide a set of columns to be sorted on when Calibre starts.
# The argument is None if saved sort history is to be used
# otherwise it is a list of column,order pairs. Column is the
# lookup/search name, found using the tooltip for the column
# Order is 0 for ascending, 1 for descending.
# For example, set it to [('authors',0),('title',0)] to sort by
# title within authors.
sort_columns_at_startup = [('authors', 0), ('series', 0), ('pubdate', 0)]


#: Set the list of words considered to be "articles" for sort strings
# ID: per_language_title_sort_articles
# Set the list of words that are to be considered 'articles' when computing the
# title sort strings. The articles differ by language. By default, calibre uses
# a combination of articles from English and whatever language the calibre user
# interface is set to. In addition, in some contexts where the book language is
# available, the language of the book is used. You can change the list of
# articles for a given language or add a new language by editing
# per_language_title_sort_articles. To tell calibre to use a language other
# than the user interface language, set, default_language_for_title_sort. For
# example, to use German, set it to 'deu'. A value of None means the user
# interface language is used. The setting title_sort_articles is ignored
# (present only for legacy reasons).
per_language_title_sort_articles = {'ron': ('Un\\s+', 'O\\s+', 'Ni\xc5\x9fte\\s+'), 'tur': ('Bir\\s+',), 'por': ('A\\s+', 'O\\s+', 'Os\\s+', 'As\\s+', 'Um\\s+', 'Uns\\s+', 'Uma\\s+', 'Umas\\s+'), 'ita': ('Lo\\s+', 'Il\\s+', "L'", 'La\\s+', 'Gli\\s+', 'I\\s+', 'Le\\s+'), 'nld': ('De\\s+', 'Het\\s+', 'Een\\s+', "'n\\s+", "'s\\s+", 'Ene\\s+', 'Ener\\s+', 'Enes\\s+', 'Den\\s+', 'Der\\s+', 'Des\\s+', "'t\\s+"), 'spa': ('El\\s+', 'La\\s+', 'Lo\\s+', 'Los\\s+', 'Las\\s+', 'Un\\s+', 'Una\\s+', 'Unos\\s+', 'Unas\\s+'), 'fra': ('Le\\s+', 'La\\s+', "L'", 'Les\\s+', 'Un\\s+', 'Une\\s+', 'Des\\s+', 'De\\s+La\\s+', 'De\\s+', "D'"), 'ell': ('O\\s+', 'I\\s+', 'To\\s+', 'Ta\\s+', 'Tus\\s+', 'Tis\\s+', "'Enas\\s+", "'Mia\\s+", "'Ena\\s+", "'Enan\\s+"), 'eng': ('A\\s+', 'The\\s+', 'An\\s+'), 'swe': ('En\\s+', 'Ett\\s+', 'Det\\s+', 'Den\\s+', 'De\\s+'), 'deu': ('Der\\s+', 'Die\\s+', 'Das\\s+', 'Den\\s+', 'Ein\\s+', 'Eine\\s+', 'Einen\\s+', 'Dem\\s+', 'Des\\s+', 'Einem\\s+', 'Eines\\s+'), 'hun': ('A\\s+', 'Az\\s+', 'Egy\\s+'), 'afr': ("'n\\s+", 'Die\\s+')}
default_language_for_title_sort = None
title_sort_articles = '^(A|The|An)\\s+'


#: The maximum width and height for covers saved in the Calibre library
# ID: maximum_cover_size
# All covers in the Calibre library will be resized, preserving aspect ratio,
# to fit within this size. This is to prevent slowdowns caused by extremely
# large covers.
maximum_cover_size = (1200, 1600)


#: Auto increment series index
# ID: series_index_auto_increment
# The algorithm used to assign a book added to an existing series a series number.
# New series numbers assigned using this tweak are always integer values, except
# if a constant non-integer is specified.
# Possible values are:
# next - First available integer larger than the largest existing number
# first_free - First available integer larger than 0
# next_free - First available integer larger than the smallest existing number
# last_free - First available integer smaller than the largest existing number
# Return largest existing + 1 if no free number is found
# const - Assign the number 1 always
# no_change - Do not change the series index
# a number - Assign that number always. The number is not in quotes. Note that
# 0.0 can be used here.
# Examples:
# series_index_auto_increment = 'next'
# series_index_auto_increment = 'next_free'
# series_index_auto_increment = 16.5
# Set the use_series_auto_increment_tweak_when_importing tweak to True to
# use the above values when importing/adding books. If this tweak is set to
# False (the default) then the series number will be set to 1 if it is not
# explicitly set during the import. If set to True, then the
# series index will be set according to the series_index_auto_increment setting.
# Note that the use_series_auto_increment_tweak_when_importing tweak is used
# only when a value is not provided during import. If the importing regular
# expression produces a value for series_index, or if you are reading metadata
# from books and the import plugin produces a value, than that value will
# be used irrespective of the setting of the tweak.
series_index_auto_increment = 'next'
use_series_auto_increment_tweak_when_importing = False


#: Add separator after completing an author name
# ID: authors_completer_append_separator
# Should the completion separator be appended
# to the end of the completed text to
# automatically begin a new completion operation
# for authors.
# Can be either True or False
authors_completer_append_separator = False


#: Author sort name algorithm
# ID: author_sort_copy_method
# The algorithm used to copy author to author_sort
# Possible values are:
# invert: use "fn ln" -> "ln, fn"
# copy  : copy author to author_sort without modification
# comma : use 'copy' if there is a ',' in the name, otherwise use 'invert'
# nocomma : "fn ln" -> "ln fn" (without the comma)
# When this tweak is changed, the author_sort values stored with each author
# must be recomputed by right-clicking on an author in the left-hand tags pane,
# selecting 'manage authors', and pressing 'Recalculate all author sort values'.
# The author name suffixes are words that are ignored when they occur at the
# end of an author name. The case of the suffix is ignored and trailing
# periods are automatically handled. The same is true for prefixes.
# The author name copy words are a set of words which if they occur in an
# author name cause the automatically generated author sort string to be
# identical to the author name. This means that the sort for a string like Acme
# Inc. will be Acme Inc. instead of Inc., Acme
author_sort_copy_method = 'comma'
author_name_suffixes = ('Jr', 'Sr', 'Inc', 'Ph.D', 'Phd', 'MD', 'M.D', 'I', 'II', 'III', 'IV', 'Junior', 'Senior')
author_name_prefixes = ('Mr', 'Mrs', 'Ms', 'Dr', 'Prof')
author_name_copywords = ('Corporation', 'Company', 'Co.', 'Agency', 'Council', 'Committee', 'Inc.', 'Institute', 'Society', 'Club', 'Team')


#: Splitting multiple author names
# ID: authors_split_regex
# By default, calibre splits a string containing multiple author names on
# ampersands and the words "and" and "with". You can customize the splitting
# by changing the regular expression below. Strings are split on whatever the
# specified regular expression matches, in addition to ampersands.
# Default: r'(?i),?\s+(and|with)\s+'
authors_split_regex = '(?i),?\\s+(and|with)\\s+'


#: Use author sort in Tag Browser
# ID: categories_use_field_for_author_name
# Set which author field to display in the tags pane (the list of authors,
# series, publishers etc on the left hand side). The choices are author and
# author_sort. This tweak affects only what is displayed under the Authors
# category in the tags pane and content server. Please note that if you set this
# to author_sort, it is very possible to see duplicate names in the list because
# although it is guaranteed that author names are unique, there is no such
# guarantee for author_sort values. Showing duplicates won't break anything, but
# it could lead to some confusion. When using 'author_sort', the tooltip will
# show the author's name.
# Examples:
# categories_use_field_for_author_name = 'author'
# categories_use_field_for_author_name = 'author_sort'
categories_use_field_for_author_name = 'author'


#: Control partitioning of Tag Browser
# ID: categories_collapsed_name_template
# When partitioning the tags browser, the format of the subcategory label is
# controlled by a template: categories_collapsed_name_template if sorting by
# name; categories_collapsed_rating_template if sorting by average rating; and
# categories_collapsed_popularity_template if sorting by popularity. There are
# two variables available to the template: first and last. The variable 'first'
# is the initial item in the subcategory, and the variable 'last' is the final
# item in the subcategory. Both variables are 'objects'; they each have multiple
# values that are obtained by using a suffix. For example, first.name for an
# author category will be the name of the author. The sub-values available are:
# name: the printable name of the item
# count: the number of books that references this item
# avg_rating: the average rating of all the books referencing this item
# sort: the sort value. For authors, this is the author_sort for that author
# category: the category (e.g., authors, series) that the item is in.
# Note that the "r'" in front of the { is necessary if there are backslashes
# (\ characters) in the template. It doesn't hurt anything to leave it there
# even if there aren't any backslashes.
categories_collapsed_name_template = '{first.sort:shorten(4,,0)} - {last.sort:shorten(4,,0)}'
categories_collapsed_rating_template = '{first.avg_rating:4.2f:ifempty(0)} - {last.avg_rating:4.2f:ifempty(0)}'
categories_collapsed_popularity_template = '{first.count:d} - {last.count:d}'


#: Control order of categories in the tag browser
# ID: tag_browser_category_order
# Change the following dict to change the order that categories are displayed in
# the tag browser. Items are named using their lookup name, and will be sorted
# using the number supplied. The lookup name '*' stands for all names that
# otherwise do not appear. Two names with the same value will be sorted
# using the default order; the one used when the dict is empty.
# Example: tag_browser_category_order = {'series':1, 'tags':2, '*':3}
# resulting in the order series, tags, then everything else in default order.
tag_browser_category_order = {'*': 1}


#: Control how dates are displayed
# ID: gui_pubdate_display_format
# Format to be used for publication date and the timestamp (date).
# A string controlling how the publication date is displayed in the GUI
# d     the day as number without a leading zero (1 to 31)
# dd    the day as number with a leading zero (01 to 31)
# ddd   the abbreviated localized day name (e.g. 'Mon' to 'Sun').
# dddd  the long localized day name (e.g. 'Monday' to 'Sunday').
# M     the month as number without a leading zero (1-12)
# MM    the month as number with a leading zero (01-12)
# MMM   the abbreviated localized month name (e.g. 'Jan' to 'Dec').
# MMMM  the long localized month name (e.g. 'January' to 'December').
# yy    the year as two digit number (00-99)
# yyyy  the year as four digit number
# h     the hours without a leading 0 (0 to 11 or 0 to 23, depending on am/pm) '
# hh    the hours with a leading 0 (00 to 11 or 00 to 23, depending on am/pm) '
# m     the minutes without a leading 0 (0 to 59) '
# mm    the minutes with a leading 0 (00 to 59) '
# s     the seconds without a leading 0 (0 to 59) '
# ss    the seconds with a leading 0 (00 to 59) '
# ap    use a 12-hour clock instead of a 24-hour clock, with "ap"
# replaced by the localized string for am or pm '
# AP    use a 12-hour clock instead of a 24-hour clock, with "AP"
# replaced by the localized string for AM or PM '
# iso   the date with time and timezone. Must be the only format present
# For example, given the date of 9 Jan 2010, the following formats show
# MMM yyyy ==> Jan 2010    yyyy ==> 2010       dd MMM yyyy ==> 09 Jan 2010
# MM/yyyy ==> 01/2010      d/M/yy ==> 9/1/10   yy ==> 10
# publication default if not set: MMM yyyy
# timestamp default if not set: dd MMM yyyy
# last_modified_display_format if not set: dd MMM yyyy
gui_pubdate_display_format = 'MMM yyyy'
gui_timestamp_display_format = 'dd MMM yyyy'
gui_last_modified_display_format = 'dd MMM yyyy'


#: Control sorting of titles and series in the library display
# ID: title_series_sorting
# Control title and series sorting in the library view. If set to
# 'library_order', the title sort field will be used instead of the title.
# Unless you have manually edited the title sort field, leading articles such as
# The and A will be ignored. If set to 'strictly_alphabetic', the titles will be
# sorted as-is (sort by title instead of title sort). For example, with
# library_order, The Client will sort under 'C'. With strictly_alphabetic, the
# book will sort under 'T'.
# This flag affects Calibre's library display. It has no effect on devices. In
# addition, titles for books added before changing the flag will retain their
# order until the title is edited. Double-clicking on a title and hitting return
# without changing anything is sufficient to change the sort.
title_series_sorting = 'library_order'


#: Control formatting of title and series when used in templates
# ID: save_template_title_series_sorting
# Control how title and series names are formatted when saving to disk/sending
# to device. The behaviour depends on the field being processed. If processing
# title, then if this tweak is set to 'library_order', the title will be
# replaced with title_sort. If it is set to 'strictly_alphabetic', then the
# title will not be changed. If processing series, then if set to
# 'library_order', articles such as 'The' and 'An' will be moved to the end. If
# set to 'strictly_alphabetic', the series will be sent without change.
# For example, if the tweak is set to library_order, "The Lord of the Rings"
# will become "Lord of the Rings, The". If the tweak is set to
# strictly_alphabetic, it would remain "The Lord of the Rings". Note that the
# formatter function raw_field will return the base value for title and
# series regardless of the setting of this tweak.
save_template_title_series_sorting = 'library_order'


#: Specify a folder Calibre should connect to at startup
# ID: auto_connect_to_folder
# Specify a folder that Calibre should connect to at startup using
# connect_to_folder. This must be a full path to the folder. If the folder does
# not exist when Calibre starts, it is ignored. If there are '\' characters in
# the path (such as in Windows paths), you must double them.
# Examples:
# auto_connect_to_folder = 'C:\\Users\\someone\\Desktop\\testlib'
# auto_connect_to_folder = '/home/dropbox/My Dropbox/someone/library'
auto_connect_to_folder = ''


#: Specify renaming rules for SONY collections
# ID: sony_collection_renaming_rules
# Specify renaming rules for sony collections. This tweak is only applicable if
# metadata management is set to automatic. Collections on Sonys are named
# depending upon whether the field is standard or custom. A collection derived
# from a standard field is named for the value in that field. For example, if
# the standard 'series' column contains the value 'Darkover', then the
# collection name is 'Darkover'. A collection derived from a custom field will
# have the name of the field added to the value. For example, if a custom series
# column named 'My Series' contains the name 'Darkover', then the collection
# will by default be named 'Darkover (My Series)'. For purposes of this
# documentation, 'Darkover' is called the value and 'My Series' is called the
# category. If two books have fields that generate the same collection name,
# then both books will be in that collection.
# This set of tweaks lets you specify for a standard or custom field how
# the collections are to be named. You can use it to add a description to a
# standard field, for example 'Foo (Tag)' instead of the 'Foo'. You can also use
# it to force multiple fields to end up in the same collection. For example, you
# could force the values in 'series', '#my_series_1', and '#my_series_2' to
# appear in collections named 'some_value (Series)', thereby merging all of the
# fields into one set of collections.
# There are two related tweaks. The first determines the category name to use
# for a metadata field.  The second is a template, used to determines how the
# value and category are combined to create the collection name.
# The syntax of the first tweak, sony_collection_renaming_rules, is:
# {'field_lookup_name':'category_name_to_use', 'lookup_name':'name', ...}
# The second tweak, sony_collection_name_template, is a template. It uses the
# same template language as plugboards and save templates. This tweak controls
# how the value and category are combined together to make the collection name.
# The only two fields available are {category} and {value}. The {value} field is
# never empty. The {category} field can be empty. The default is to put the
# value first, then the category enclosed in parentheses, it isn't empty:
# '{value} {category:|(|)}'
# Examples: The first three examples assume that the second tweak
# has not been changed.
# 1: I want three series columns to be merged into one set of collections. The
# column lookup names are 'series', '#series_1' and '#series_2'. I want nothing
# in the parenthesis. The value to use in the tweak value would be:
# sony_collection_renaming_rules={'series':'', '#series_1':'', '#series_2':''}
# 2: I want the word '(Series)' to appear on collections made from series, and
# the word '(Tag)' to appear on collections made from tags. Use:
# sony_collection_renaming_rules={'series':'Series', 'tags':'Tag'}
# 3: I want 'series' and '#myseries' to be merged, and for the collection name
# to have '(Series)' appended. The renaming rule is:
# sony_collection_renaming_rules={'series':'Series', '#myseries':'Series'}
# 4: Same as example 2, but instead of having the category name in parentheses
# and appended to the value, I want it prepended and separated by a colon, such
# as in Series: Darkover. I must change the template used to format the category name
# The resulting two tweaks are:
# sony_collection_renaming_rules={'series':'Series', 'tags':'Tag'}
# sony_collection_name_template='{category:||: }{value}'
sony_collection_renaming_rules = {}
sony_collection_name_template = '{value}{category:| (|)}'


#: Specify how SONY collections are sorted
# ID: sony_collection_sorting_rules
# Specify how sony collections are sorted. This tweak is only applicable if
# metadata management is set to automatic. You can indicate which metadata is to
# be used to sort on a collection-by-collection basis. The format of the tweak
# is a list of metadata fields from which collections are made, followed by the
# name of the metadata field containing the sort value.
# Example: The following indicates that collections built from pubdate and tags
# are to be sorted by the value in the custom column '#mydate', that collections
# built from 'series' are to be sorted by 'series_index', and that all other
# collections are to be sorted by title. If a collection metadata field is not
# named, then if it is a series- based collection it is sorted by series order,
# otherwise it is sorted by title order.
# [(['pubdate', 'tags'],'#mydate'), (['series'],'series_index'), (['*'], 'title')]
# Note that the bracketing and parentheses are required. The syntax is
# [ ( [list of fields], sort field ) , ( [ list of fields ] , sort field ) ]
# Default: empty (no rules), so no collection attributes are named.
sony_collection_sorting_rules = []


#: Control how tags are applied when copying books to another library
# ID: add_new_book_tags_when_importing_books
# Set this to True to ensure that tags in 'Tags to add when adding
# a book' are added when copying books to another library.
add_new_book_tags_when_importing_books = False


#: Set the maximum number of tags to show per book in the content server
# ID: max_content_server_tags_shown
max_content_server_tags_shown = 5


#: Set custom metadata fields that the content server will or will not display.
# ID: content_server_will_display
# content_server_will_display is a list of custom fields to be displayed.
# content_server_wont_display is a list of custom fields not to be displayed.
# wont_display has priority over will_display.
# The special value '*' means all custom fields. The value [] means no entries.
# Defaults:
# content_server_will_display = ['*']
# content_server_wont_display = []
# Examples:
# To display only the custom fields #mytags and #genre:
# content_server_will_display = ['#mytags', '#genre']
# content_server_wont_display = []
# To display all fields except #mycomments:
# content_server_will_display = ['*']
# content_server_wont_display['#mycomments']
content_server_will_display = ['*']
content_server_wont_display = []


#: Set the maximum number of sort 'levels'
# ID: maximum_resort_levels
# Set the maximum number of sort 'levels' that Calibre will use to resort the
# library after certain operations such as searches or device insertion. Each
# sort level adds a performance penalty. If the database is large (thousands of
# books) the penalty might be noticeable. If you are not concerned about multi-
# level sorts, and if you are seeing a slowdown, reduce the value of this tweak.
maximum_resort_levels = 5


#: Choose whether dates are sorted using visible fields
# ID: sort_dates_using_visible_fields
# Date values contain both a date and a time. When sorted, all the fields are
# used, regardless of what is displayed. Set this tweak to True to use only
# the fields that are being displayed.
sort_dates_using_visible_fields = False


#: Specify which font to use when generating a default cover or masthead
# ID: generate_cover_title_font
# Absolute path to .ttf font files to use as the fonts for the title, author
# and footer when generating a default cover or masthead image. Useful if the
# default font (Liberation Serif) does not contain glyphs for the language of
# the books in your library.
generate_cover_title_font = None
generate_cover_foot_font = None


#: Fuzz value for trimming covers
# ID: cover_trim_fuzz_value
# The value used for the fuzz distance when trimming a cover.
# Colors within this distance are considered equal.
# The distance is in absolute intensity units.
cover_trim_fuzz_value = 10


#: Control behavior of the book list
# ID: doubleclick_on_library_view
# You can control the behaviour of doubleclicks on the books list.
# Choices: open_viewer, do_nothing,
# edit_cell, edit_metadata. Selecting edit_metadata has the side effect of
# disabling editing a field using a single click.
# Default: open_viewer.
# Example: doubleclick_on_library_view = 'do_nothing'
# You can also control whether the book list scrolls horizontally per column or
# per pixel. Default is per column.
doubleclick_on_library_view = 'open_viewer'
horizontal_scrolling_per_column = True


#: Language to use when sorting.
# ID: locale_for_sorting
# Setting this tweak will force sorting to use the
# collating order for the specified language. This might be useful if you run
# Calibre in English but want sorting to work in the language where you live.
# Set the tweak to the desired ISO 639-1 language code, in lower case.
# You can find the list of supported locales at
# http://publib.boulder.ibm.com/infocenter/iseries/v5r3/topic/nls/rbagsicusortsequencetables.htm
# Default: locale_for_sorting = '' -- use the language calibre displays in
# Example: locale_for_sorting = 'fr' -- sort using French rules.
# Example: locale_for_sorting = 'nb' -- sort using Norwegian rules.
locale_for_sorting = ''


#: Number of columns for custom metadata in the edit metadata dialogue.
# ID: metadata_single_use_2_cols_for_custom_fields
# Set whether to use one or two columns for custom metadata, when editing
# metadata one book at a time. If True, then the fields are laid out using two
# columns. If False, one column is used.
metadata_single_use_2_cols_for_custom_fields = True


#: Order of custom column(s) in edit metadata
# ID: metadata_edit_custom_column_order
# Controls the order that custom columns are listed in edit metadata single
# and bulk. The columns listed in the tweak are displayed first and in the
# order provided. Any columns not listed are dislayed after the listed ones,
# in alphabetical order. Do note that this tweak does not change the size of
# the edit widgets. Putting comments widgets in this list may result in some
# odd widget spacing when using two-column mode.
# Enter a comma-separated list of custom field lookup names, as in
# metadata_edit_custom_column_order = ['#genre', '#mytags', '#etc']
metadata_edit_custom_column_order = []


#: The number of seconds to wait before sending emails
# ID: public_smtp_relay_delay
# The number of seconds to wait before sending emails when using a
# public email server like gmail or hotmail. Default is: 5 minutes
# Setting it to lower may cause the server's SPAM controls to kick in,
# making email sending fail. Changes will take effect only after a restart of
# Calibre.
public_smtp_relay_delay = 301


#: Where to send downloaded news
# ID: send_news_to_device_location
# When automatically sending downloaded news to a connected device, Calibre
# will by default send it to the main memory. By changing this tweak, you can
# control where it is sent. Valid values are "main", "carda", "cardb". Note
# that if there isn't enough free space available on the location you choose,
# the files will be sent to the location with the most free space.
send_news_to_device_location = 'main'


#: Which interfaces the content server should listen on
# ID: server_listen_on
# By default, the Calibre content server listens on '0.0.0.0' which means that it
# accepts IPv4 connections on all interfaces. You can change this to, for
# example, '127.0.0.1' to only listen for connections from the local machine, or
# to '::' to listen to all incoming IPv6 and IPv4 connections (this may not
# work on all operating systems)
server_listen_on = '0.0.0.0'


#: Unified toolbar on OS X
# ID: unified_title_toolbar_on_osx
# If you enable this option and restart Calibre, the toolbar will be 'unified'
# with the titlebar as is normally for OS X applications. However, doing this has
# various bugs, for instance the minimum width of the toolbar becomes twice
# what it should be and it causes other random bugs on some systems, so turn it
# on at your own risk!
unified_title_toolbar_on_osx = False


#: Save original file when converting/polishing from same format to same format
# ID: save_original_format
# When calibre does a conversion from the same format to the same format, for
# example, from EPUB to EPUB, the original file is saved, so that in case the
# conversion is poor, you can tweak the settings and run it again. By setting
# this to False you can prevent calibre from saving the original file.
# Similarly, by setting save_original_format_when_polishing to False you can
# prevent calibre from saving the original file when polishing.
save_original_format = True
save_original_format_when_polishing = True


#: Number of recently viewed books to show
# ID: gui_view_history_size
# Right-clicking the View button shows a list of recently viewed books. Control
# how many should be shown, here.
gui_view_history_size = 15


#: Change the font size of book details in the interface
# ID: change_book_details_font_size_by
# Change the font size at which book details are rendered in the side panel and
# comments are rendered in the metadata edit dialogue. Set it to a positive or
# negative number to increase or decrease the font size.
change_book_details_font_size_by = 0


#: Compile General Program Mode templates to Python
# ID: compile_gpm_templates
# Compiled general program mode templates are significantly faster than
# interpreted templates. Setting this tweak to True causes calibre to compile
# (in most cases) general program mode templates. Setting it to False causes
# calibre to use the old behaviour -- interpreting the templates. Set the tweak
# to False if some compiled templates produce incorrect values.
# Default:    compile_gpm_templates = True
# No compile: compile_gpm_templates = False
compile_gpm_templates = True


#: What format to default to when using the Tweak feature
# ID: default_tweak_format
# The Tweak feature of calibre allows direct editing of a book format.
# If multiple formats are available, calibre will offer you a choice
# of formats, defaulting to your preferred output format if it is available.
# Set this tweak to a specific value of 'EPUB' or 'AZW3' to always default
# to that format rather than your output format preference.
# Set to a value of 'remember' to use whichever format you chose last time you
# used the Tweak feature.
# Examples:
# default_tweak_format = None       (Use output format)
# default_tweak_format = 'EPUB'
# default_tweak_format = 'remember'
default_tweak_format = None


#: Do not preselect a completion when editing authors/tags/series/etc.
# ID: preselect_first_completion
# This means that you can make changes and press Enter and your changes will
# not be overwritten by a matching completion. However, if you wish to use the
# completions you will now have to press Tab to select one before pressing
# Enter. Which technique you prefer will depend on the state of metadata in
# your library and your personal editing style.
preselect_first_completion = False


#: Completion mode when editing authors/tags/series/etc.
# ID: completion_mode
# By default, when completing items, calibre will show you all the candidates
# that start with the text you have already typed. You can instead have it show
# all candidates that contain the text you have already typed. To do this, set
# completion_mode to 'contains'. For example, if you type asi it will match both
# Asimov and Quasimodo, whereas the default behavior would match only Asimov.
completion_mode = 'prefix'


#: Recognize numbers inside text when sorting
# ID: numeric_collation
# This means that when sorting on text fields like title the text "Book 2"
# will sort before the text "Book 100". If you want this behavior, set
# numeric_collation = True note that doing so will cause problems with text
# that starts with numbers and is a little slower.
numeric_collation = False


#: Sort the list of libraries alphabetically
# ID: many_libraries
# The list of libraries in the Copy to Library and Quick Switch menus are
# normally sorted by most used. However, if there are more than a certain
# number of such libraries, the sorting becomes alphabetic. You can set that
# number here. The default is ten libraries.
many_libraries = 10


#: Highlight the virtual library name when using a Virtual Library
# ID: highlight_virtual_library
# The virtual library name next to the Virtual Library button is highlighted in
# yellow when using a Virtual Library. You can choose the color used for the
# highlight with this tweak. Set it to 'transparent' to disable highlighting.
highlight_virtual_library = 'yellow'


#: Choose available output formats for conversion
# ID: restrict_output_formats
# Restrict the list of available output formats in the conversion dialogs.
# For example, if you only want to convert to EPUB and AZW3, change this to
# restrict_output_formats = ['EPUB', 'AZW3']. The default value of None causes
# all available output formats to be present.
restrict_output_formats = None


#: Set the thumbnail image quality used by the content server
# ID: content_server_thumbnail_compression_quality
# The quality of a thumbnail is largely controlled by the compression quality
# used when creating it. Set this to a larger number to improve the quality.
# Note that the thumbnails get much larger with larger compression quality
# numbers.
# The value can be between 50 and 99
content_server_thumbnail_compression_quality = 75



# The following are tweaks for installed plugins

tweak_book_prefer = 'epub'


completion_change_to_ascii_sorting = 2500


draw_hidden_section_indicators = True


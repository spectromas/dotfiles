# calibre wide preferences

### Begin group: DEFAULT
 
# database path
# Path to the database in which books are stored
database_path = '/home/alex/library1.db'
 
# filename pattern
# Pattern to guess metadata from filenames
filename_pattern = u'(?P<title>.+) - (?P<author>[^_]+)'
 
# isbndb com key
# Access key for isbndb.com
isbndb_com_key = ''
 
# network timeout
# Default timeout for network operations (seconds)
network_timeout = 5
 
# library path
# Path to directory in which your library of books is stored
library_path = u'/home/alex/Documents/Ebooks Library'
 
# language
# The language in which to display the user interface
language = 'en_GB'
 
# output format
# The default output format for ebook conversions.
output_format = 'epub'
 
# input format order
# Ordered list of formats to prefer for input.
input_format_order = cPickle.loads('\x80\x02]q\x01(X\x04\x00\x00\x00EPUBq\x02X\x04\x00\x00\x00MOBIq\x03X\x03\x00\x00\x00LITq\x04X\x03\x00\x00\x00PRCq\x05X\x03\x00\x00\x00FB2q\x06X\x04\x00\x00\x00HTMLq\x07X\x03\x00\x00\x00HTMq\x08X\x04\x00\x00\x00XHTMq\tX\x05\x00\x00\x00SHTMLq\nX\x05\x00\x00\x00XHTMLq\x0bX\x03\x00\x00\x00ZIPq\x0cX\x03\x00\x00\x00ODTq\rX\x03\x00\x00\x00RTFq\x0eX\x03\x00\x00\x00PDFq\x0fX\x03\x00\x00\x00TXTq\x10X\x04\x00\x00\x00TEXTq\x11X\x06\x00\x00\x00RECIPEq\x12X\x04\x00\x00\x00DJVUq\x13X\x03\x00\x00\x00AZWq\x14X\x03\x00\x00\x00CBCq\x15X\x04\x00\x00\x00AZW4q\x16X\x04\x00\x00\x00PMLZq\x17X\x04\x00\x00\x00POBIq\x18X\x03\x00\x00\x00RARq\x19X\x02\x00\x00\x00RBq\x1aX\x03\x00\x00\x00PMLq\x1bX\x05\x00\x00\x00HTMLZq\x1cX\x04\x00\x00\x00DOCXq\x1dX\x08\x00\x00\x00MARKDOWNq\x1eX\x03\x00\x00\x00DJVq\x1fX\x11\x00\x00\x00DOWNLOADED_RECIPEq X\x03\x00\x00\x00CHMq!X\x03\x00\x00\x00TCRq"X\x04\x00\x00\x00DOCMq#X\x04\x00\x00\x00SHTMq$X\x04\x00\x00\x00UPDBq%X\x02\x00\x00\x00MDq&X\x04\x00\x00\x00AZW3q\'X\x03\x00\x00\x00SNBq(X\x03\x00\x00\x00LRFq)X\x03\x00\x00\x00CBRq*X\x03\x00\x00\x00OPFq+X\x04\x00\x00\x00TXTZq,X\x03\x00\x00\x00CBZq-X\x03\x00\x00\x00PDBq.X\x07\x00\x00\x00TEXTILEq/e.')
 
# read file metadata
# Read metadata from files
read_file_metadata = True
 
# worker process priority
# The priority of worker processes. A higher priority means they run faster and consume more resources. Most tasks like conversion/news download/adding books/etc. are affected by this setting.
worker_process_priority = 'normal'
 
# swap author names
# Swap author first and last names when reading metadata
swap_author_names = False
 
# add formats to existing
# Add new formats to existing book records
add_formats_to_existing = False
 
# check for dupes on ctl
# Check for duplicates when copying to another library
check_for_dupes_on_ctl = False
 
# installation uuid
# Installation UUID
installation_uuid = '0836aacc-37d6-4781-b4f9-024feba78f67'
 
# new book tags
# Tags to apply to books added to the library
new_book_tags = cPickle.loads('\x80\x02]q\x01.')
 
# mark new books
# Mark newly added books. The mark is a temporary mark that is automatically removed when calibre is restarted.
mark_new_books = False
 
# saved searches
# List of named saved searches
saved_searches = cPickle.loads('\x80\x02}q\x01.')
 
# user categories
# User-created tag browser categories
user_categories = cPickle.loads('\x80\x02}q\x01.')
 
# manage device metadata
# How and when calibre updates metadata on the device.
manage_device_metadata = 'manual'
 
# limit search columns
# When searching for text without using lookup prefixes, as for example, Red instead of title:Red, limit the columns searched to those named below.
limit_search_columns = False
 
# limit search columns to
# Choose columns to be searched when not using prefixes, as for example, when searching for Red instead of title:Red. Enter a list of search/lookup names separated by commas. Only takes effect if you set the option to limit search columns above.
limit_search_columns_to = cPickle.loads('\x80\x02]q\x01(U\x05titleq\x02U\x07authorsq\x03U\x04tagsq\x04U\x06seriesq\x05U\tpublisherq\x06e.')
 
# use primary find in search
# Characters typed in the search box will match their accented versions, based on the language you have chosen for the calibre interface. For example, in  English, searching for n will match ñ and n, but if your language is Spanish it will only match n. Note that this is much slower than a simple search on very large libraries.
use_primary_find_in_search = True
 
# migrated
# For Internal use. Don't modify.
migrated = False
 



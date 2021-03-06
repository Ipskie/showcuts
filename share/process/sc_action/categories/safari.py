from share.process.components._directory import *
from ..action import *

class _base(action):
    category = 'SAFARI'
    glyph = 'system/Safari.jpg'

class searchweb(_base):
    name = 'Search Web'
    title = [
        text('Search'),
        choose(
            'WFSearchWebDestination',
            ask_each_time='Service',
            default='Google',
            options=[
                'Amazon',
                'Bing',
                'DuckDuckGo',
                'eBay',
                'Google',
                'Reddit',
                'Twitter',
                'Yahoo!',
                'YouTube',
            ],
        ),
        text('for'),
        inline(
            'WFInputText',
            blank_text='Text',
            ask_each_time='Text',
        ),
    ]

class showwebpage(_base):
    name = 'Show Web Page'
    title = [
        text('Show web page at'),
        inline(
            'WFURL',
            blank_text='URL',
            ask_each_time='Text',
        ),
    ]
    lines = [
        line_toggle(
            'Enter Safari Reader',
            'WFEnterSafariReader',
            default=False,
            ask_each_time='Ask Each Time',
        ),
    ]

class readinglist(_base):
    name = 'Add to Reading List'
    title = [
        text('Add'),
        list_inline(
            'WFURL',
            blank_text='URL',
            ask_each_time='Text',
        ),
        text('to Reading List'),
    ]

class openurl(_base):
    name = 'Open URLs'
    title = [
        text('Open'),
        list_inline(
            'WFInput',
            blank_text='URL',
            ask_each_time='Text',
        ),
    ]
    # also found this code:
    # title_elem = [
    #     'Open',
    #     make_magic(component.parameters, 'WFInput', 'Safari web page'),
    # ]

class runjavascriptonwebpage(_base):
    name = 'Run JavaScript on Web Page'
    result = 'JavaScript Result'
    title = [
        text('Run JavaScript on'),
        magic(
            'WFInput',
            blank_text='Web page',
            ask_each_time=None,
        ),
    ]
    lines = [
        line_code(
            'WFJavaScript',
            default='''var result = [];
// Get all links from the page
var elements = document.querySelectorAll("a");
for (let element of elements) {
	result.push({
		"url": element.href,
		"text": element.innerText
	});
}

// Call completion to finish
completion(result);''',
            blank_text='JavaScript',
        ),
    ]

class getwebpagecontents(_base):
    name = 'Get Contents of Web Page'
    title = [
        text('Get contents of web page at'),
        inline(
            'WFInput',
            blank_text='URL',
            ask_each_time='Text',
        ),
    ]
    result = 'Contents of Web Page'

class getarticle(_base):
    name = 'Get Article using Safari Reader'
    title = [
        text('Get article from'),
        inline(
            'WFWebPage',
            blank_text='URL',
            ask_each_time='Text',
        ),
    ]
    result = 'Article'

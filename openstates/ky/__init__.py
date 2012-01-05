metadata = dict(
    name='Kentucky',
    abbreviation='ky',
    legislature_name='Kentucky General Assembly',
    upper_chamber_name='Senate',
    lower_chamber_name='House of Representatives',
    upper_chamber_title='Senator',
    lower_chamber_title='Representative',
    upper_chamber_term=4,
    lower_chamber_term=2,
    terms=[
    #dict(name='2009',
    #    start_year=2009,
    #    end_year=2009,
    #    sessions=[
    #        '2009 Regular Session',
    #        '2009 Special Session'
    #        ]),
    #dict(name='2010',
    #    start_year=2010,
    #    end_year=2010,
    #    sessions=[
    #        '2010 Regular Session',
    #        '2010 Extraordinary Session'
    #        ]),
    dict(name='2011-2012',
        start_year=2011,
        end_year=2011,
        sessions=[
            '2011 Regular Session'
            ])
    ],
    session_details={
        #'2009 Regular Session': {'type': 'primary',
        #                         'display_name': '2009 Regular Session'},
        #'2009 Special Session': {'type': 'special',
        #                         'display_name': '2009 Special Session'},
        #'2010 Regular Session': {'type': 'primary',
        #                         'display_name': '2010 Regular Session'},
        #'2010 Extraordinary Session': {
        #    'type': 'special', 'display_name': '2010 Extraordinary Session',
        #},
        '2011 Regular Session': {'type': 'primary',
                                 'display_name': '2011 Regular Session'}
    },
    feature_flags=['subjects', 'events'],
)

def session_list():
    from billy.scrape.utils import url_xpath
    return url_xpath('http://www.lrc.ky.gov/legislation.htm',
                     '//a[contains(@href, "record.htm")]/img/@alt')

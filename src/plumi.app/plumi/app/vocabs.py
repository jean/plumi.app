from zope.i18nmessageid import MessageFactory
_ = MessageFactory("plumi")

vocab_set = {}

taxonomy_sub_folder={'topic':'video_categories','genre':'video_genre','callouts':'submission_categories','countries':'video_countries','languages':'video_languages'}

vocab_set['video_countries'] = (
         ('XX', _('-- International --')),
         ('AF', _(u'Afghanistan')),
         ('AL', _(u'Albania')),
         ('DZ', _(u'Algeria ')),
         ('AS', _(u'American Samoa')),
         ('AD', _(u'Andorra ')),
         ('AO', _(u'Angola')),
         ('AI', _(u'Anguilla')),
         ('AQ', _(u'Antarctica')),
         ('AG', _(u'Antigua And Barbuda ')),
         ('AR', _(u'Argentina ')),
         ('AM', _(u'Armenia ')),
         ('AW', _(u'Aruba ')),
         ('AU', _(u'Australia ')),
         ('AT', _(u'Austria ')),
         ('AZ', _(u'Azerbaijan')),
         ('BS', _(u'Bahamas ')),
         ('BH', _(u'Bahrain ')),
         ('BD', _(u'Bangladesh')),
         ('BB', _(u'Barbados')),
         ('BY', _(u'Belarus ')),
         ('BE', _(u'Belgium ')),
         ('BZ', _(u'Belize')),
         ('BJ', _(u'Benin ')),
         ('BM', _(u'Bermuda ')),
         ('BT', _(u'Bhutan')),
         ('BO', _(u'Bolivia ')),
         ('BA', _(u'Bosnia And Herzegowina')),
         ('BW', _(u'Botswana')),
         ('BV', _(u'Bouvet Island ')),
         ('BR', _(u'Brazil')),
         ('IO', _(u'British Indian Ocean Territory')),
         ('BN', _(u'Brunei Darussalam ')),
         ('BG', _(u'Bulgaria')),
         ('BF', _(u'Burkina Faso')),
         ('BI', _(u'Burundi ')),
         ('KH', _(u'Cambodia')),
         ('CM', _(u'Cameroon')),
         ('CA', _(u'Canada')),
         ('CV', _(u'Cape Verde')),
         ('KY', _(u'Cayman Islands')),
         ('CF', _(u'Central African Republic')),
         ('TD', _(u'Chad')),
         ('CL', _(u'Chile ')),
         ('CN', _(u'China ')),
         ('CX', _(u'Christmas Island')),
         ('CC', _(u'Cocos (Keeling) Islands ')),
         ('CO', _(u'Colombia')),
         ('KM', _(u'Comoros ')),
         ('CD', _(u'Congo, Democratic Republic Of (Was Zaire) ')),
         ('CG', _(u'Congo, People\'s Republic Of ')),
         ('CK', _(u'Cook Islands')),
         ('CR', _(u'Costa Rica')),
         ('CI', _(u'Cote D\'ivoire ')),
         ('HR', _(u'Croatia (Local Name: Hrvatska)')),
         ('CU', _(u'Cuba')),
         ('CY', _(u'Cyprus')),
         ('CZ', _(u'Czech Republic')),
         ('DK', _(u'Denmark ')),
         ('DJ', _(u'Djibouti')),
         ('DM', _(u'Dominica')),
         ('DO', _(u'Dominican Republic')),
         ('EC', _(u'Ecuador ')),
         ('EG', _(u'Egypt ')),
         ('SV', _(u'El Salvador ')),
         ('GQ', _(u'Equatorial Guinea ')),
         ('ER', _(u'Eritrea ')),
         ('EE', _(u'Estonia ')),
         ('ET', _(u'Ethiopia')),
         ('FK', _(u'Falkland Islands (Malvinas) ')),
         ('FO', _(u'Faroe Islands ')),
         ('FJ', _(u'Fiji')),
         ('FI', _(u'Finland ')),
         ('FR', _(u'France')),
         ('FX', _(u'France, Metropolitan')),
         ('GF', _(u'French Guiana ')),
         ('PF', _(u'French Polynesia')),
         ('TF', _(u'French Southern Territories ')),
         ('GA', _(u'Gabon ')),
         ('GM', _(u'Gambia')),
         ('GE', _(u'Georgia ')),
         ('DE', _(u'Germany ')),
         ('GH', _(u'Ghana ')),
         ('GI', _(u'Gibraltar ')),
         ('GR', _(u'Greece')),
         ('GL', _(u'Greenland ')),
         ('GD', _(u'Grenada ')),
         ('GP', _(u'Guadeloupe')),
         ('GU', _(u'Guam')),
         ('GT', _(u'Guatemala ')),
         ('GN', _(u'Guinea')),
         ('GW', _(u'Guinea-Bissau ')),
         ('GY', _(u'Guyana')),
         ('HT', _(u'Haiti ')),
         ('HM', _(u'Heard And Mc Donald Islands ')),
         ('HN', _(u'Honduras')),
         ('HK', _(u'Hong Kong ')),
         ('HU', _(u'Hungary ')),
         ('IS', _(u'Iceland ')),
         ('IN', _(u'India ')),
         ('ID', _(u'Indonesia ')),
         ('IR', _(u'Iran (Islamic Republic Of)')),
         ('IQ', _(u'Iraq')),
         ('IE', _(u'Ireland ')),
         ('IL', _(u'Israel')),
         ('IT', _(u'Italy ')),
         ('JM', _(u'Jamaica ')),
         ('JP', _(u'Japan ')),
         ('JO', _(u'Jordan')),
         ('KZ', _(u'Kazakhstan')),
         ('KE', _(u'Kenya ')),
         ('KI', _(u'Kiribati')),
         ('KP', _(u'Korea, Democratic People\'s Republic Of')),
         ('KR', _(u'Korea, Republic Of')),
         ('KW', _(u'Kuwait')),
         ('KG', _(u'Kyrgyzstan')),
         ('LA', _(u'Lao People\'s Democratic Republic')),
         ('LV', _(u'Latvia')),
         ('LB', _(u'Lebanon ')),
         ('LS', _(u'Lesotho ')),
         ('LR', _(u'Liberia ')),
         ('LY', _(u'Libyan Arab Jamahiriya')),
         ('LI', _(u'Liechtenstein ')),
         ('LT', _(u'Lithuania ')),
         ('LU', _(u'Luxembourg')),
         ('MO', _(u'Macau ')),
         ('MK', _(u'Macedonia, The Former Yugoslav Republic Of')),
         ('MG', _(u'Madagascar')),
         ('MW', _(u'Malawi')),
         ('MY', _(u'Malaysia')),
         ('MV', _(u'Maldives')),
         ('ML', _(u'Mali')),
         ('MT', _(u'Malta ')),
         ('MH', _(u'Marshall Islands')),
         ('MQ', _(u'Martinique')),
         ('MR', _(u'Mauritania')),
         ('MU', _(u'Mauritius ')),
         ('YT', _(u'Mayotte ')),
         ('MX', _(u'Mexico')),
         ('FM', _(u'Micronesia, Federated States Of ')),
         ('MD', _(u'Moldova, Republic Of')),
         ('MC', _(u'Monaco')),
         ('MN', _(u'Mongolia')),
         ('MS', _(u'Montserrat')),
         ('MA', _(u'Morocco ')),
         ('MZ', _(u'Mozambique')),
         ('MM', _(u'Myanmar ')),
         ('NA', _(u'Namibia ')),
         ('NR', _(u'Nauru ')),
         ('NP', _(u'Nepal ')),
         ('NL', _(u'Netherlands ')),
         ('AN', _(u'Netherlands Antilles')),
         ('NC', _(u'New Caledonia ')),
         ('NZ', _(u'New Zealand ')),
         ('NI', _(u'Nicaragua ')),
         ('NE', _(u'Niger ')),
         ('NG', _(u'Nigeria ')),
         ('NU', _(u'Niue')),
         ('NF', _(u'Norfolk Island')),
         ('MP', _(u'Northern Mariana Islands')),
         ('NO', _(u'Norway')),
         ('OM', _(u'Oman')),
         ('PK', _(u'Pakistan')),
         ('PW', _(u'Palau ')),
         ('PS', _(u'Palestinian Territory, Occupied ')),
         ('PA', _(u'Panama')),
         ('PG', _(u'Papua New Guinea')),
         ('PY', _(u'Paraguay')),
         ('PE', _(u'Peru')),
         ('PH', _(u'Philippines ')),
         ('PN', _(u'Pitcairn')),
         ('PL', _(u'Poland')),
         ('PT', _(u'Portugal')),
         ('PR', _(u'Puerto Rico ')),
         ('QA', _(u'Qatar ')),
         ('RE', _(u'Reunion ')),
         ('RO', _(u'Romania ')),
         ('RU', _(u'Russian Federation')),
         ('RW', _(u'Rwanda')),
         ('KN', _(u'Saint Kitts And Nevis ')),
         ('LC', _(u'Saint Lucia ')),
         ('VC', _(u'Saint Vincent And The Grenadines')),
         ('WS', _(u'Samoa ')),
         ('SM', _(u'San Marino')),
         ('ST', _(u'Sao Tome And Principe ')),
         ('SA', _(u'Saudi Arabia')),
         ('SN', _(u'Senegal ')),
         ('SC', _(u'Seychelles')),
         ('SL', _(u'Sierra Leone')),
         ('SG', _(u'Singapore ')),
         ('SK', _(u'Slovakia (Slovak Republic)')),
         ('SI', _(u'Slovenia')),
         ('SB', _(u'Solomon Islands ')),
         ('SO', _(u'Somalia ')),
         ('ZA', _(u'South Africa')),
         ('GS', _(u'South Georgia And The South Sandwich Islands')),
         ('ES', _(u'Spain ')),
         ('LK', _(u'Sri Lanka ')),
         ('SH', _(u'St. Helena')),
         ('PM', _(u'St. Pierre And Miquelon ')),
         ('SD', _(u'Sudan ')),
         ('SR', _(u'Suriname')),
         ('SJ', _(u'Svalbard And Jan Mayen Islands')),
         ('SZ', _(u'Swaziland ')),
         ('SE', _(u'Sweden')),
         ('CH', _(u'Switzerland ')),
         ('SY', _(u'Syrian Arab Republic')),
         ('TW', _(u'Taiwan')),
         ('TJ', _(u'Tajikistan')),
         ('TZ', _(u'Tanzania, United Republic Of')),
         ('TH', _(u'Thailand')),
         ('TL', _(u'Timor-Leste')),
         ('TG', _(u'Togo')),
         ('TK', _(u'Tokelau ')),
         ('TO', _(u'Tonga ')),
         ('TT', _(u'Trinidad And Tobago ')),
         ('TN', _(u'Tunisia ')),
         ('TR', _(u'Turkey')),
         ('TM', _(u'Turkmenistan')),
         ('TC', _(u'Turks And Caicos Islands')),
         ('TV', _(u'Tuvalu')),
         ('UG', _(u'Uganda')),
         ('UA', _(u'Ukraine ')),
         ('AE', _(u'United Arab Emirates')),
         ('GB', _(u'United Kingdom')),
         ('US', _(u'United States ')),
         ('UM', _(u'United States Minor Outlying Islands')),
         ('UY', _(u'Uruguay ')),
         ('UZ', _(u'Uzbekistan')),
         ('VU', _(u'Vanuatu ')),
         ('VA', _(u'Vatican City State (Holy See) ')),
         ('VE', _(u'Venezuela ')),
         ('VN', _(u'Viet Nam')),
         ('VG', _(u'Virgin Islands (British)')),
         ('VI', _(u'Virgin Islands (U.S.) ')),
         ('WF', _(u'Wallis And Futuna Islands ')),
         ('EH', _(u'Western Sahara')),
         ('YE', _(u'Yemen ')),
         ('RS', _(u'Serbia')),
         ('ZM', _(u'Zambia')),
         ('ZW', _(u'Zimbabwe')),
        )

vocab_set['video_categories'] = (
         ('art', _(u'Art / Culture')),
         ('internet', _(u'Internet')),
        )
vocab_set['video_genre'] = (
         ('documentary', _(u'Documentary')),
         ('fiction', _(u'Fiction')),
         ('animation', _(u'Animation')),
        )
vocab_set['submission_categories'] = (
         ('dvd', _(u'DVD')),
         ('production', _(u'Production')),
         ('other', _(u'Other')),
        ) 
vocab_set['video_languages'] = (
        ('aa', _(u'Afar ')),
        ('ab', _(u'Abkhazian ')),
        ('af', _(u'Afrikaans ')),
        ('am', _(u'Amharic ')),
        ('ar', _(u'Arabic ')),
        ('as', _(u'Assamese ')),
        ('ay', _(u'Aymara ')),
        ('az', _(u'Azerbaijani ')),
        ('ba', _(u'Bashkir ')),
        ('be', _(u'Byelorussian ')),
        ('bg', _(u'Bulgarian ')),
        ('bh', _(u'Bihari ')),
        ('bi', _(u'Bislama ')),
        ('bn', _(u'Bengali;')),
        ('bo', _(u'Tibetan ')),
        ('br', _(u'Breton ')),
        ('ca', _(u'Catalan ')),
        ('co', _(u'Corsican ')),
        ('cs', _(u'Czech ')),
        ('cy', _(u'Welsh ')),
        ('da', _(u'Danish ')),
        ('de', _(u'German ')),
        ('dz', _(u'Bhutani ')),
        ('el', _(u'Greek ')),
        ('en', _(u'English ')),
        ('eo', _(u'Esperanto ')),
        ('es', _(u'Spanish ')),
        ('et', _(u'Estonian ')),
        ('eu', _(u'Basque ')),
        ('fa', _(u'Persian ')),
        ('fi', _(u'Finnish ')),
        ('fj', _(u'Fiji ')),
        ('fo', _(u'Faroese ')),
        ('fr', _(u'French ')),
        ('fy', _(u'Frisian ')),
        ('ga', _(u'Irish ')),
        ('gd', _(u'Scots')),
        ('gl', _(u'Galician ')),
        ('gn', _(u'Guarani ')),
        ('gu', _(u'Gujarati ')),
        ('ha', _(u'Hausa ')),
        ('he', _(u'Hebrew')),
        ('hi', _(u'Hindi ')),
        ('hr', _(u'Croatian ')),
        ('hu', _(u'Hungarian ')),
        ('hy', _(u'Armenian ')),
        ('ia', _(u'Interlingua ')),
        ('id', _(u'Indonesian')),
        ('ie', _(u'Interlingue ')),
        ('ik', _(u'Inupiak ')),
        ('is', _(u'Icelandic ')),
        ('it', _(u'Italian ')),
        ('iu', _(u'Inuktitut ')),
        ('ja', _(u'Japanese ')),
        ('jw', _(u'Javanese ')),
        ('ka', _(u'Georgian ')),
        ('kk', _(u'Kazakh ')),
        ('kl', _(u'Greenlandic ')),
        ('km', _(u'Cambodian ')),
        ('kn', _(u'Kannada ')),
        ('ko', _(u'Korean ')),
        ('ks', _(u'Kashmiri ')),
        ('ku', _(u'Kurdish ')),
        ('ky', _(u'Kirghiz ')),
        ('la', _(u'Latin ')),
        ('ln', _(u'Lingala ')),
        ('lo', _(u'Laothian ')),
        ('lt', _(u'Lithuanian ')),
        ('lv', _(u'Latvian')),
        ('mg', _(u'Malagasy ')),
        ('mi', _(u'Maori ')),
        ('mk', _(u'Macedonian ')),
        ('ml', _(u'Malayalam ')),
        ('mn', _(u'Mongolian ')),
        ('mo', _(u'Moldavian ')),
        ('mr', _(u'Marathi ')),
        ('ms', _(u'Malay ')),
        ('mt', _(u'Maltese ')),
        ('my', _(u'Burmese ')),
        ('na', _(u'Nauru ')),
        ('ne', _(u'Nepali ')),
        ('nl', _(u'Dutch ')),
        ('no', _(u'Norwegian ')),
        ('oc', _(u'Occitan ')),
        ('om', _(u'Afan')),
        ('or', _(u'Oriya ')),
        ('pa', _(u'Punjabi ')),
        ('pl', _(u'Polish ')),
        ('ps', _(u'Pashto')),
        ('pt', _(u'Portuguese ')),
        ('qu', _(u'Quechua ')),
        ('rm', _(u'Rhaeto-Romance ')),
        ('rn', _(u'Kirundi ')),
        ('ro', _(u'Romanian ')),
        ('ru', _(u'Russian ')),
        ('rw', _(u'Kinyarwanda ')),
        ('sa', _(u'Sanskrit ')),
        ('sd', _(u'Sindhi ')),
        ('sg', _(u'Sangho ')),
        ('sh', _(u'Serbo-Croatian ')),
        ('si', _(u'Sinhalese ')),
        ('sk', _(u'Slovak ')),
        ('sl', _(u'Slovenian ')),
        ('sm', _(u'Samoan ')),
        ('sn', _(u'Shona ')),
        ('so', _(u'Somali ')),
        ('sq', _(u'Albanian ')),
        ('sr', _(u'Serbian ')),
        ('ss', _(u'Siswati ')),
        ('st', _(u'Sesotho ')),
        ('su', _(u'Sundanese ')),
        ('sv', _(u'Swedish ')),
        ('sw', _(u'Swahili ')),
        ('ta', _(u'Tamil ')),
        ('te', _(u'Telugu ')),
        ('tg', _(u'Tajik ')),
        ('th', _(u'Thai ')),
        ('ti', _(u'Tigrinya ')),
        ('tk', _(u'Turkmen ')),
        ('tl', _(u'Tagalog ')),
        ('tn', _(u'Setswana ')),
        ('to', _(u'Tonga ')),
        ('tr', _(u'Turkish ')),
        ('ts', _(u'Tsonga ')),
        ('tt', _(u'Tatar ')),
        ('tw', _(u'Twi ')),
        ('ug', _(u'Uighur ')),
        ('uk', _(u'Ukrainian ')),
        ('ur', _(u'Urdu ')),
        ('uz', _(u'Uzbek ')),
        ('vi', _(u'Vietnamese ')),
        ('vo', _(u'Volapuk ')),
        ('wo', _(u'Wolof ')),
        ('xh', _(u'Xhosa ')),
        ('yi', _(u'Yiddish')),
        ('yo', _(u'Yoruba ')),
        ('za', _(u'Zhuang ')),
        ('zh', _(u'Chinese ')),
        ('zu', _(u'Zulu ')),
       ) 


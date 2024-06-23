def get_states():
    states = ["Other - International", "Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii",
              "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", 
              "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", 
              "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
    return states

def get_countries():
    #List from https://gist.github.com/chidimo/bc38a85a6aaac6ebb900ca43dd2075e9
    
    countries_and_code = ['AFGHANISTAN - AF', 'ALBANIA - AL', 'ALGERIA - DZ', 'AMERICAN SAMOA - AS', 'ANDORRA - AD', 'ANGOLA - AO', 'ANGUILLA - AI', 'ANTARCTICA - AQ',
                          'ANTIGUA AND BARBUDA - AG', 'ARGENTINA - AR', 'ARMENIA - AM', 'ARUBA - AW', 'AUSTRALIA - AU', 'AUSTRIA - AT', 'AZERBAIJAN - AZ', 'BAHAMAS - BS', 
                          'BAHRAIN - BH', 'BANGLADESH - BD', 'BARBADOS - BB', 'BELARUS - BY', 'BELGIUM - BE', 'BELIZE - BZ', 'BENIN - BJ', 'BERMUDA - BM', 'BHUTAN - BT', 
                          'BOLIVIA - BO', 'BOSNIA AND HERZEGOVINA - BA', 'BOTSWANA - BW', 'BOUVET ISLAND - BV', 'BRAZIL - BR', 'BRITISH INDIAN OCEAN TERRITORY - IO', 
                          'BRUNEI DARUSSALAM - BN', 'BULGARIA - BG', 'BURKINA FASO - BF', 'BURUNDI - BI', 'CAMBODIA - KH', 'CAMEROON - CM', 'CANADA - CA', 'CAPE VERDE - CV', 
                          'CAYMAN ISLANDS - KY', 'CENTRAL AFRICAN REPUBLIC - CF', 'CHAD - TD', 'CHILE - CL', 'CHINA - CN', 'CHRISTMAS ISLAND - CX', 
                          'COCOS (KEELING) ISLANDS - CC', 'COLOMBIA - CO', 'COMOROS - KM', 'CONGO - CG', 'CONGO, THE DEMOCRATIC REPUBLIC OF - CD', 'COOK ISLANDS - CK', 
                          'COSTA RICA - CR', "CÃ”TE D'IVOIRE - CI", 'CROATIA - HR', 'CUBA - CU', 'CYPRUS - CY', 'CZECH REPUBLIC - CZ', 'DENMARK - DK', 'DJIBOUTI - DJ', 
                          'DOMINICA - DM', 'DOMINICAN REPUBLIC - DO', 'ECUADOR - EC', 'EGYPT - EG', 'EL SALVADOR - SV', 'EQUATORIAL GUINEA - GQ', 'ERITREA - ER', 'ESTONIA - EE', 
                          'ETHIOPIA - ET', 'FALKLAND ISLANDS (MALVINAS) - FK', 'FAROE ISLANDS - FO', 'FIJI - FJ', 'FINLAND - FI', 'FRANCE - FR', 'FRENCH GUIANA - GF', 
                          'FRENCH POLYNESIA - PF', 'FRENCH SOUTHERN TERRITORIES - TF', 'GABON - GA', 'GAMBIA - GM', 'GEORGIA - GE', 'GERMANY - DE', 'GHANA - GH', 'GIBRALTAR - GI', 
                          'GREECE - GR', 'GREENLAND - GL', 'GRENADA - GD', 'GUADELOUPE - GP', 'GUAM - GU', 'GUATEMALA - GT', 'GUINEA - GW', 'GUYANA - GY', 'HAITI - HT', 
                          'HEARD ISLAND AND MCDONALD ISLANDS - HM', 'HONDURAS - HN', 'HONG KONG - HK', 'HUNGARY - HU', 'ICELAND - IS', 'INDIA - IN', 'INDONESIA - ID', 
                          'IRAN, ISLAMIC REPUBLIC OF - IR', 'IRAQ - IQ', 'IRELAND - IE', 'ISRAEL - IL', 'ITALY - IT', 'JAMAICA - JM', 'JAPAN - JP', 'JORDAN - JO', 
                          'KAZAKHSTAN - KZ', 'KENYA - KE', 'KIRIBATI - KI', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF - KP", 'KOREA, REPUBLIC OF - KR', 'KUWAIT - KW', 
                          'KYRGYZSTAN - KG', "LAO PEOPLE'S DEMOCRATIC REPUBLIC - LA", 'LATVIA - LV', 'LEBANON - LB', 'LESOTHO - LS', 'LIBERIA - LR', 'LIBYAN ARAB JAMAHIRIYA - LY', 
                          'LIECHTENSTEIN - LI', 'LITHUANIA - LT', 'LUXEMBOURG - LU', 'MACAO - MO', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF - MK', 'MADAGASCAR - MG', 
                          'MALAWI - MW', 'MALAYSIA - MY', 'MALDIVES - MV', 'MALI - ML', 'MALTA - MT', 'MARSHALL ISLANDS - MH', 'MARTINIQUE - MQ', 'MAURITANIA - MR', 'MAURITIUS - MU', 
                          'MAYOTTE - YT', 'MEXICO - MX', 'MICRONESIA, FEDERATED STATES OF - FM', 'MOLDOVA, REPUBLIC OF - MD', 'MONACO - MC', 'MONGOLIA - MN', 'MONTSERRAT - MS', 
                          'MOROCCO - MA', 'MOZAMBIQUE - MZ', 'MYANMAR - MM', 'NAMIBIA - NA', 'NAURU - NR', 'NEPAL - NP', 'NETHERLANDS - NL', 'NETHERLANDS ANTILLES - AN', 
                          'NEW CALEDONIA - NC', 'NEW ZEALAND - NZ', 'NICARAGUA - NI', 'NIGER - NE', 'NIGERIA - NG', 'NIUE - NU', 'NORFOLK ISLAND - NF', 
                          'NORTHERN MARIANA ISLANDS - MP', 'NORWAY - NO', 'OMAN - OM', 'PAKISTAN - PK', 'PALAU - PW', 'PALESTINIAN TERRITORY - PS', 'PANAMA - PA', 
                          'PAPUA NEW GUINEA - PG', 'PARAGUAY - PY', 'PERU - PE', 'PHILIPPINES - PH', 'PITCAIRN - PN', 'POLAND - PL', 'PORTUGAL - PT', 'PUERTO RICO - PR', 
                          'QATAR - QA', 'RÃ‰UNION - RE', 'ROMANIA - RO', 'RUSSIAN FEDERATION - RU', 'RWANDA - RW', 'SAINT HELENA - SH', 'SAINT KITTS AND NEVIS - KN', 
                          'SAINT LUCIA - LC', 'SAINT PIERRE AND MIQUELON - PM', 'SAINT VINCENT AND THE GRENADINES - VC', 'SAMOA - WS', 'SAN MARINO - SM', 'SAO TOME AND PRINCIPE - ST', 
                          'SAUDI ARABIA - SA', 'SENEGAL - SN', 'SERBIA AND MONTENEGRO - CS', 'SEYCHELLES - SC', 'SIERRA LEONE - SL', 'SINGAPORE - SG', 'SLOVAKIA - SK', 
                          'SLOVENIA - SI', 'SOLOMON ISLANDS - SB', 'SOMALIA - SO', 'SOUTH AFRICA - ZA', 'SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS - GS', 'SPAIN - ES', 
                          'SRI LANKA - LK', 'SUDAN - SD', 'SURINAME - SR', 'SVALBARD AND JAN MAYEN - SJ', 'SWAZILAND - SZ', 'SWEDEN - SE', 'SWITZERLAND - CH', 
                          'SYRIAN ARAB REPUBLIC - SY', 'TAIWAN, PROVINCE OF CHINA - TW', 'TAJIKISTAN - TJ', 'TANZANIA, UNITED REPUBLIC OF - TZ', 'THAILAND - TH', 
                          'TIMOR - TL', 'TOGO - TG', 'TOKELAU - TK', 'TONGA - TO', 'TRINIDAD AND TOBAGO - TT', 'TUNISIA - TN', 'TURKEY - TR', 'TURKMENISTAN - TM', 
                          'TURKS AND CAICOS ISLANDS - TC', 'TUVALU - TV', 'UGANDA - UG', 'UKRAINE - UA', 'UNITED ARAB EMIRATES - AE', 'UNITED KINGDOM - GB', 
                          'UNITED STATES - US', 'UNITED STATES MINOR OUTLYING ISLANDS - UM', 'URUGUAY - UY', 'UZBEKISTAN - UZ', 'VANUATU - VU', 'VIET NAM - VN', 
                          'VIRGIN ISLANDS, BRITISH - VG', 'VIRGIN ISLANDS, U.S. - VI', 'WALLIS AND FUTUNA - WF', 'WESTERN SAHARA - EH', 'YEMEN - YE', 'ZIMBABWE - ZW']
    
    return countries_and_code

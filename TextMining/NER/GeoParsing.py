from mordecai import Geoparser
from geopy.geocoders import Nominatim
#import pyap
country_codes = {
"ABW" :  "Aruba",
"AFG" : "Afghanistan",
"AGO": "Angola",
"AIA" :"Anguilla",
"ALA" :  "Åland Islands",
"ALB" : "Albania",
"AND" :  "Andorra",
"ANT" : "Netherlands Antilles",
"ARE" : "United Arab Emirates",
"ARG" :  "Argentina",
"ARM" : "Armenia",
"ASM" : "American Samoa",
"ATA" : "Antarctica",
"ATF" :  "French Southern Territories",
"ATG" :  "Antigua and Barbuda",
"AUS" : "Australia",
"AUT" : "Austria",
"AZE" : "Azerbaijan",
"BDI" : "Burundi",
"BEL" : "Belgium",
"BEN" : "Benin",
"BFA" : "Burkina Faso",
"BGD" : "Bangladesh",
"BGR" : "Bulgaria",
"BHR" : "Bahrain",
"BHS" : "Bahamas",
"BIH" : "Bosnia and Herzegovina",
"BLM" : "Saint Barthélemy",
"BLR" : "Belarus",
"BLZ" :  "Belize",
"BMU" :  "Bermuda",
"BOL" : "Bolivia",
"BRA" : "Brazil",
"BRB" : "Barbados",
"BRN" : "Brunei Darussalam",
"BTN" : "Bhutan",
"BVT" : "Bouvet Island",
"BWA" : "Botswana",
"CAF" : "Central African Republic",
"CAN" : "Canada",
"CCK" : "Cocos (Keeling) Islands",
"CHE" : "Switzerland",
"CHL" : "Chile",
"CHN" :  "China",
"CIV" : "Cote d'Ivoire",
"CMR" : "Cameroon",
"COD" : "Congo, the Democratic Republic of the",
"COG" : "Congo",
"COK" :  "Cook Islands",
"COL" :  "Colombia",
"COM" : "Comoros",
"CPV" : "Cape Verde",
"CRI" : "Costa Rica",
"CUB" : "Cuba",
"CXR" : "Christmas Island",
"CYM" :  "Cayman Islands",
"CYP" : "Cyprus",
"CZE" : "Czech Republic",
"DEU" : "Germany",
"DJI" : "Djibouti",
"DMA" : "Dominica",
"DNK" : "Denmark",
"DOM" : "Dominican Republic",
"DZA" : "Algeria",
"ECU" : "Ecuador",
"EGY" : "Egypt",
"ERI" : "Eritrea",
"ESH" : "Western Sahara",
"ESP" : "Spain",
"EST" : "Estonia",
"ETH" : "Ethiopia",
"FIN" : "Finland",
"FJI" :  "Fiji",
"FLK" :  "Falkland Islands (Malvinas)",
"FRA" : "France",
"FRO" : "Faroe Islands",
"FSM" : "Micronesia, Federated States of",
"GAB" : "Gabon",
"GBR" : "UK",
"GEO" : "Georgia",
"GGY" : "Guernsey",
"GHA" :  "Ghana",
"GIB" : "Gibraltar",
"GIN" : "Guinea",
"GLP" : "Guadeloupe",
"GMB" : "Gambia",
"GNB" : "Guinea-Bissau",
"GNQ" : "Equatorial Guinea",
"GRC" : "Greece",
"GRD" : "Grenada",
"GRL" : "Greenland",
"GTM" : "Guatemala",
"GUF" : "French Guiana",
"GUM" : "Guam",
"GUY" : "Guyana",
"HKG" : "Hong Kong",
"HMD" :  "Heard Island and McDonald Islands",
"HND" : "Honduras",
"HRV" : "Croatia",
"HTI" : "Haiti",
"HUN" : "Hungary",
"IDN" : "Indonesia",
"IMN" : "Isle of Man",
"IND" : "India",
"IOT" : "British Indian Ocean Territory",
"IRL" : "Ireland",
"IRN" : "Iran, Islamic Republic of",
"IRQ" : "Iraq",
"ISL" : "Iceland",
"ISR" : "Israel",
"ITA" : "Italy",
"JAM" : "Jamaica",
"JEY" : "Jersey",
"JOR" : "Jordan",
"JPN" : "Japan",
"KAZ" : "Kazakhstan",
"KEN" : "Kenya",
"KGZ" : "Kyrgyzstan",
"KHM" : "Cambodia",
"KIR" : "Kiribati",
"KNA" : "Saint Kitts and Nevis",
"KOR" : "Korea",
"KWT" :  "Kuwait",
"LAO" : "Lao People's Democratic Republic",
"LBN" : "Lebanon",
"LBR" : "Liberia",
"LBY" : "Libyan Arab Jamahiriya",
"LCA" : "Saint Lucia",
"LIE" : "Liechtenstein",
"LKA" : "Sri Lanka",
"LSO" :  "Lesotho",
"LTU" : "Lithuania",
"LUX" : "Luxembourg",
"LVA" :  "Latvia",
"MAC" : "Macao",
"MAF" :  "Saint Martin (French part)",
"MAR" : "Morocco",
"MCO" : "Monaco",
"MDA" : "Moldova",
"MDG" : "Madagascar",
"MDV" : "Maldives",
"MEX" : "Mexico",
"MHL" : "Marshall Islands",
"MKD" : "Macedonia",
"MLI" : "Mali",
"MLT" : "Malta",
"MMR" : "Myanmar",
"MNE" : "Montenegro",
"MNG" : "Mongolia",
"MNP" : "Northern Mariana Islands",
"MOZ" : "Mozambique",
"MRT" : "Mauritania",
"MSR" : "Montserrat",
"MTQ" : "Martinique",
"MUS" : "Mauritius",
"MWI" : "Malawi",
"MYS" : "Malaysia",
"MYT" : "Mayotte",
"NAM" : "Namibia",
"NCL" : "New Caledonia",
"NER" : "Niger",
"NFK" : "Norfolk Island",
"NGA" : "Nigeria",
"NIC" : "Nicaragua",
"NIU" : "Niue",
"NLD" : "Netherlands",
"NOR" : "Norway",
"NPL" : "Nepal",
"NRU" : "Nauru",
"NZL" : "New Zealand",
"OMN" : "Oman",
"PAK" : "Pakistan",
"PAN" : "Panama",
"PCN" : "Pitcairn",
"PER" : "Peru",
"PHL" : "Philippines",
"PLW" : "Palau",
"PNG" : "Papua New Guinea",
"POL" : "Poland",
"PRI" : "Puerto Rico",
"PRK" : "Democratic People's Republic of Korea",
"PRT" : "Portugal",
"PRY" : "Paraguay",
"PSE" : "Palestine",
"PYF" : "French Polynesia",
"QAT" : "Qatar",
"REU" : "Reunion",
"ROU" : "Romania",
"RUS" : "Russia",
"RWA" : "Rwanda",
"SAU" : "Saudi Arabia",
"SDN" : "Sudan",
"SEN" : "Senegal",
"SGP" : "Singapore",
"SGS" : "South Georgia and the South Sandwich Islands",
"SHN" : "Saint Helena, Ascension and Tristan da Cunha",
"SJM" : "Svalbard and Jan Mayen",
"SLB" : "Solomon Islands",
"SLE" : "Sierra Leone",
"SLV" : "El Salvador",
"SMR" : "San Marino",
"SOM" : "Somalia",
"SPM" : "Saint Pierre and Miquelon",
"SRB" : "Serbia",
"STP" : "Sao Tome and Principe",
"SUR" : "Suriname",
"SVK" : "Slovakia",
"SVN" : "Slovenia",
"SWE" : "Sweden",
"SWZ" : "Swaziland",
"SYC" : "Seychelles",
"SYR" : "Syria",
"TCA" : "Turks and Caicos Islands",
"TCD" : "Chad",
"TGO" : "Togo",
"THA" : "Thailand",
"TJK" : "Tajikistan",
"TKL" : "Tokelau",
"TKM" : "Turkmenistan",
"TLS" : "Timor-Leste",
"TON" : "Tonga",
"TTO" : "Trinidad and Tobago",
"TUN" : "Tunisia",
"TUR" : "Turkey",
"TUV" : "Tuvalu",
"TWN" : "Taiwan, Province of China",
"TZA" : "Tanzania",
"UGA" : "Uganda",
"UKR" : "Ukraine",
"UMI" : "United States Minor Outlying Islands",
"URY" : "Uruguay",
"USA" : "USA",
"UZB" : "Uzbekistan",
"VAT" : "Vatican City State",
"VCT" : "Saint Vincent and the Grenadines",
"VEN" : "Venezuela",
"VGB" : "Virgin Islands",
"VIR" : "Virgin Islands, U.S.",
"VNM" : "Viet Nam",
"VUT" : "Vanuatu",
"WLF" : "Wallis and Futuna",
"WSM" : "Samoa",
"YEM" : "Yemen",
"ZAF" : "South Africa",
"ZMB" : "Zambia",
"ZWE" :  "Zimbabwe"
}

geo = Geoparser()
naa = geo.geoparse("Belgrade")
print(naa)
code = naa[0]['country_predicted']
print (country_codes[code])
naa = geo.geoparse("Germany")
code = naa[0]['country_predicted']
print (country_codes[code])
naa = geo.geoparse("Europe")
print(naa)
code = naa[0]['country_predicted']
print (country_codes[code])

#baa = geo.geoparse("Pedje Milosavljevica 74, Belgrade, Serbia")
#print(baa)
#geolocator = Nominatim()
#location = geolocator.geocode("Pedje Milosavljevica 74, Belgrade, Serbia")
#print(location.address)

#test_address = """
#    Lorem ipsum 225 E. John Carpenter Freeway, Suite 1500 Irving, Texas 75062 Dorem sit amet
#    """
#addresses = pyap.parse(test_address, country='US')
#for address in addresses:
#    print(address)
    # shows address parts
#    print(address.as_dict())
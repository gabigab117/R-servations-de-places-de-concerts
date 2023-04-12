# Generated by Django 4.1.7 on 2023-04-12 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="nom de l'adresse")),
                ('address_1', models.CharField(help_text='Voirie, numéro de rue', max_length=1024, verbose_name='Adresse 1')),
                ('address_2', models.CharField(blank=True, help_text='Bât, étage, lieu-dit', max_length=1024, verbose_name='Adresse 2')),
                ('city', models.CharField(max_length=1024, verbose_name='Commune')),
                ('zip_code', models.CharField(max_length=32, verbose_name='Code Postal')),
                ('country', models.CharField(choices=[('af', 'Afghanistan'), ('ax', 'Åland Islands'), ('al', 'Albania'), ('dz', 'Algeria'), ('as', 'American Samoa'), ('ad', 'Andorra'), ('ao', 'Angola'), ('ai', 'Anguilla'), ('aq', 'Antarctica'), ('ag', 'Antigua and Barbuda'), ('ar', 'Argentina'), ('am', 'Armenia'), ('aw', 'Aruba'), ('au', 'Australia'), ('at', 'Austria'), ('az', 'Azerbaijan'), ('bs', 'Bahamas'), ('bh', 'Bahrain'), ('bd', 'Bangladesh'), ('bb', 'Barbados'), ('by', 'Belarus'), ('be', 'Belgium'), ('bz', 'Belize'), ('bj', 'Benin'), ('bm', 'Bermuda'), ('bt', 'Bhutan'), ('bo', 'Bolivia, Plurinational State of'), ('bq', 'Bonaire, Sint Eustatius and Saba'), ('ba', 'Bosnia and Herzegovina'), ('bw', 'Botswana'), ('bv', 'Bouvet Island'), ('br', 'Brazil'), ('io', 'British Indian Ocean Territory'), ('bn', 'Brunei Darussalam'), ('bg', 'Bulgaria'), ('bf', 'Burkina Faso'), ('bi', 'Burundi'), ('kh', 'Cambodia'), ('cm', 'Cameroon'), ('ca', 'Canada'), ('cv', 'Cabo Verde'), ('ky', 'Cayman Islands'), ('cf', 'Central African Republic'), ('td', 'Chad'), ('cl', 'Chile'), ('cn', 'China'), ('cx', 'Christmas Island'), ('cc', 'Cocos (Keeling) Islands'), ('co', 'Colombia'), ('km', 'Comoros'), ('cg', 'Congo'), ('cd', 'Congo, Democratic Republic of the'), ('ck', 'Cook Islands'), ('cr', 'Costa Rica'), ('ci', "Côte d'Ivoire"), ('hr', 'Croatia'), ('cu', 'Cuba'), ('cw', 'Curaçao'), ('cy', 'Cyprus'), ('cz', 'Czechia'), ('dk', 'Denmark'), ('dj', 'Djibouti'), ('dm', 'Dominica'), ('do', 'Dominican Republic'), ('ec', 'Ecuador'), ('eg', 'Egypt'), ('sv', 'El Salvador'), ('gq', 'Equatorial Guinea'), ('er', 'Eritrea'), ('ee', 'Estonia'), ('et', 'Ethiopia'), ('fk', 'Falkland Islands (Malvinas)'), ('fo', 'Faroe Islands'), ('fj', 'Fiji'), ('fi', 'Finland'), ('fr', 'France'), ('gf', 'French Guiana'), ('pf', 'French Polynesia'), ('tf', 'French Southern Territories'), ('ga', 'Gabon'), ('gm', 'Gambia'), ('ge', 'Georgia'), ('de', 'Germany'), ('gh', 'Ghana'), ('gi', 'Gibraltar'), ('gr', 'Greece'), ('gl', 'Greenland'), ('gd', 'Grenada'), ('gp', 'Guadeloupe'), ('gu', 'Guam'), ('gt', 'Guatemala'), ('gg', 'Guernsey'), ('gn', 'Guinea'), ('gw', 'Guinea-Bissau'), ('gy', 'Guyana'), ('ht', 'Haiti'), ('hm', 'Heard Island and McDonald Islands'), ('va', 'Holy See'), ('hn', 'Honduras'), ('hk', 'Hong Kong'), ('hu', 'Hungary'), ('is', 'Iceland'), ('in', 'India'), ('id', 'Indonesia'), ('ir', 'Iran, Islamic Republic of'), ('iq', 'Iraq'), ('ie', 'Ireland'), ('im', 'Isle of Man'), ('il', 'Israel'), ('it', 'Italy'), ('jm', 'Jamaica'), ('jp', 'Japan'), ('je', 'Jersey'), ('jo', 'Jordan'), ('kz', 'Kazakhstan'), ('ke', 'Kenya'), ('ki', 'Kiribati'), ('kp', "Korea, Democratic People's Republic of"), ('kr', 'Korea, Republic of'), ('xk', 'Kosovo'), ('kw', 'Kuwait'), ('kg', 'Kyrgyzstan'), ('la', "Lao People's Democratic Republic"), ('lv', 'Latvia'), ('lb', 'Lebanon'), ('ls', 'Lesotho'), ('lr', 'Liberia'), ('ly', 'Libya'), ('li', 'Liechtenstein'), ('lt', 'Lithuania'), ('lu', 'Luxembourg'), ('mo', 'Macao'), ('mk', 'North Macedonia'), ('mg', 'Madagascar'), ('mw', 'Malawi'), ('my', 'Malaysia'), ('mv', 'Maldives'), ('ml', 'Mali'), ('mt', 'Malta'), ('mh', 'Marshall Islands'), ('mq', 'Martinique'), ('mr', 'Mauritania'), ('mu', 'Mauritius'), ('yt', 'Mayotte'), ('mx', 'Mexico'), ('fm', 'Micronesia, Federated States of'), ('md', 'Moldova, Republic of'), ('mc', 'Monaco'), ('mn', 'Mongolia'), ('me', 'Montenegro'), ('ms', 'Montserrat'), ('ma', 'Morocco'), ('mz', 'Mozambique'), ('mm', 'Myanmar'), ('na', 'Namibia'), ('nr', 'Nauru'), ('np', 'Nepal'), ('nl', 'Netherlands'), ('nc', 'New Caledonia'), ('nz', 'New Zealand'), ('ni', 'Nicaragua'), ('ne', 'Niger'), ('ng', 'Nigeria'), ('nu', 'Niue'), ('nf', 'Norfolk Island'), ('mp', 'Northern Mariana Islands'), ('no', 'Norway'), ('om', 'Oman'), ('pk', 'Pakistan'), ('pw', 'Palau'), ('ps', 'Palestine, State of'), ('pa', 'Panama'), ('pg', 'Papua New Guinea'), ('py', 'Paraguay'), ('pe', 'Peru'), ('ph', 'Philippines'), ('pn', 'Pitcairn'), ('pl', 'Poland'), ('pt', 'Portugal'), ('pr', 'Puerto Rico'), ('qa', 'Qatar'), ('re', 'Réunion'), ('ro', 'Romania'), ('ru', 'Russian Federation'), ('rw', 'Rwanda'), ('bl', 'Saint Barthélemy'), ('sh', 'Saint Helena, Ascension and Tristan da Cunha'), ('kn', 'Saint Kitts and Nevis'), ('lc', 'Saint Lucia'), ('mf', 'Saint Martin (French part)'), ('pm', 'Saint Pierre and Miquelon'), ('vc', 'Saint Vincent and the Grenadines'), ('ws', 'Samoa'), ('sm', 'San Marino'), ('st', 'Sao Tome and Principe'), ('sa', 'Saudi Arabia'), ('sn', 'Senegal'), ('rs', 'Serbia'), ('sc', 'Seychelles'), ('sl', 'Sierra Leone'), ('sg', 'Singapore'), ('sx', 'Sint Maarten (Dutch part)'), ('sk', 'Slovakia'), ('si', 'Slovenia'), ('sb', 'Solomon Islands'), ('so', 'Somalia'), ('za', 'South Africa'), ('gs', 'South Georgia and the South Sandwich Islands'), ('ss', 'South Sudan'), ('es', 'Spain'), ('lk', 'Sri Lanka'), ('sd', 'Sudan'), ('sr', 'Suriname'), ('sj', 'Svalbard and Jan Mayen'), ('sz', 'Eswatini'), ('se', 'Sweden'), ('ch', 'Switzerland'), ('sy', 'Syrian Arab Republic'), ('tw', 'Taiwan, Province of China'), ('tj', 'Tajikistan'), ('tz', 'Tanzania, United Republic of'), ('th', 'Thailand'), ('tl', 'Timor-Leste'), ('tg', 'Togo'), ('tk', 'Tokelau'), ('to', 'Tonga'), ('tt', 'Trinidad and Tobago'), ('tn', 'Tunisia'), ('tr', 'Türkiye'), ('tm', 'Turkmenistan'), ('tc', 'Turks and Caicos Islands'), ('tv', 'Tuvalu'), ('ug', 'Uganda'), ('ua', 'Ukraine'), ('ae', 'United Arab Emirates'), ('gb', 'United Kingdom of Great Britain and Northern Ireland'), ('us', 'United States of America'), ('um', 'United States Minor Outlying Islands'), ('uy', 'Uruguay'), ('uz', 'Uzbekistan'), ('vu', 'Vanuatu'), ('ve', 'Venezuela, Bolivarian Republic of'), ('vn', 'Viet Nam'), ('vg', 'Virgin Islands, British'), ('vi', 'Virgin Islands, U.S.'), ('wf', 'Wallis and Futuna'), ('eh', 'Western Sahara'), ('ye', 'Yemen'), ('zm', 'Zambia'), ('zw', 'Zimbabwe')], max_length=2)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
        ),
    ]

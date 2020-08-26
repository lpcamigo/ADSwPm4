import re
tup_list=[]
with open('raw_playoff_data.txt','r') as p_data:
    header = p_data.readline()
    for lin in p_data.readlines():
        try:
            upset = 'No'
            year = re.findall(r'^([1-2]{1}[0-9]{3})',lin)[0]
            round = re.findall(r'^[1-2]{1}[0-9]{3}\t{2}([A-Za-z ]+)\t',lin)[0]
            teams = re.findall(r'([A-Za-z0-9 ]+ \([1-8]\))',lin)
            rankings = re.findall(r'\(([1-8])\)', lin)
            series_winner = teams[0]
            if int(rankings[0]) > int(rankings[1]):
                upset = 'Yes'
            else:
                upset = 'No'
            if int(year) < 1970:
                p_format = 'older formats'
            elif int(year) < 1975:
                p_format = '1970 format'
            elif int(year) < 1977:
                p_format = '1975 format'
            elif int(year) < 1984:
                p_format = '1977 format'
            elif int(year) < 2003:
                p_format = '1984 format'
            elif int(year) < 2005:
                p_format = '2003 format'
            elif int(year) < 2007:
                p_format = '2005 format'
            elif int(year) < 2016:
                p_format = '2007 format'
            elif int(year) >= 2016:
                p_format = '2016 format'
            tup_list.append((year, round, teams, series_winner, upset, p_format))
        except:
            continue

with open('filtered_p_data.csv','w') as out_file:
    out_file.write('Year,Round,Team 1(Ranking),Team 2(Ranking),Series Winner(Ranking),Upset?,Playoff Format')
    out_file.write('\n')
    for year, round, teams, series_winner, upset,p_format in tup_list:
        out_file.write(f'{year},{round},{teams[0]},{teams[1]},{series_winner},{upset},{p_format}')
        out_file.write('\n')

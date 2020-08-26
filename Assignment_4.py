import pandas as pd
import matplotlib.pyplot as plt

upset_dict={}
df = pd.read_csv('filtered_p_data.csv',header=0)
for year, data in df.groupby('Year'):
    upset_dict[year] = data[data['Upset?'] == 'Yes'].shape[0]
#print(upset_dict)
reformat_years=[1947,1949,1950,1951,1954,1955,1958,1961,1967,1968,1970,1975,1977,1984,2003,2005,2007,2016]
vals = pd.Series(upset_dict)
#print(vals)
plt.figure()
plt.plot(vals, color='k',label='Number of Upsets')
for item in reformat_years:
    if item >= 2003:
        plt.axvline(x=item,linewidth=0.5, linestyle='-',ymin=0.2,ymax=1)
    else:
        plt.axvline(x=item,linewidth=0.5, linestyle='-')
plt.title('Upsets in NBA Playoff History (1947-2019)', fontsize=12)
plt.legend(['Number of Upsets','Playoff Reformat'],loc=4,frameon=False)
plt.show()

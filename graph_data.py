import matplotlib.pyplot as plt

### Takes data and visualizes average main stats from each decade
def graph_main_stats(stats):
   
    points = []
    assists = []
    rebounds = []
    era = ['80s','90s','00s','10s']
   
    for decade in stats:
       points.append(decade[2])
       assists.append(decade[15])
       rebounds.append(decade[14])
       
    plt.plot(era, points, label='Points')
    plt.plot(era, assists, label='Assists')
    plt.plot(era, rebounds, label='Rebounds')
    plt.xlabel("Eras")
    plt.ylabel("Stats")
    plt.title("How Mainline Stats Changed in Each Era")
    plt.legend()
    plt.savefig('How_Mainline_Stats_Changed_in_Each_Era.pdf')
   
    
    
    


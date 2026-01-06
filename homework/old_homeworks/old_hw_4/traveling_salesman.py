def calc_total_distance(table_of_distances, city_order):
    '''
    Calculates distances between a sequence of cities.
    
    Inputs: N x N table containing distances between each pair of the N
    cities, as well as an array of length N+1 containing the city order,
    which starts and ends with the same city (ensuring that the path is
    closed)

    Returns: total path length for the closed loop.
    '''
    total_distance = 0.0

    # loop over cities and sum up the path length between successive pairs
    for i in range(city_order.size-1):
        total_distance += table_of_distances[city_order[i]][city_order[i+1]]

    return total_distance


def plot_cities(city_order,city_x,city_y):
    '''
    Plots cities and the path between them.
    
    Inputs: ordering of cities, x and y coordinates of each city.  
    
    Returns: a plot showing the cities and the path between them.
    '''
    
    # first make x,y arrays
    x = []
    y = []

    # put together arrays of x and y positions that show the order that the
    # salesman traverses the cities
    for i in range(0, city_order.size):
        x.append(city_x[city_order[i]])
        y.append(city_y[city_order[i]])

    # append the first city onto the end so the loop is closed
    x.append(city_x[city_order[0]])
    y.append(city_y[city_order[0]])

    #time.sleep(0.1)  
    clear_output(wait=True)
    display(fig)            # Reset display
    fig.clear()             # clear output for animation

    plt.xlim(-0.2, 20.2)    # give a little space around the edges of the plot
    plt.ylim(-0.2, 20.2)
    
    # plot city positions in blue, and path in red.
    plt.plot(city_x,city_y, 'bo', x, y, 'r-')


'''
This code sets up everything we need!

Given a number of cities, set up random x and y positions and calculate a
table of distances between pairs of cities (used for calculating the total
trip distance).  Then set up an array that controls the order that the
salesman travels between cities, and plots out the initial path.
'''

# number of cities we'll use.
number_of_cities = 30

# seed for random number generator so we get the same value every time!
np.random.seed(2024561414)

# create random x,y positions for our current number of cities.  (Distance scaling is arbitrary.)
city_x = np.random.random(size=number_of_cities)*20.0
city_y = np.random.random(size=number_of_cities)*20.0

# table of city distances - empty for the moment
city_distances = np.zeros((number_of_cities,number_of_cities))

# calculate distnace between each pair of cities and store it in the table.
# technically we're calculating 2x as many things as we need (as well as the
# diagonal, which should all be zeros), but whatever, it's cheap.
for a in range(number_of_cities):
    for b in range(number_of_cities):
        city_distances[a][b] = ((city_x[a]-city_x[b])**2 + (city_y[a]-city_y[b])**2 )**0.5

# create the array of cities in the order we're going to go through them
city_order = np.arange(city_distances.shape[0])

# tack on the first city to the end of the array, since that ensures a closed loop
city_order = np.append(city_order, city_order[0])

fig = plt.figure()

# Put your code here!



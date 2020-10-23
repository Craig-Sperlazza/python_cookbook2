# https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen

# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

def avg_dict(dict, query_name):
    for name, scores in dict.items():
        if name == query_name:
            sum = 0
            new_list = scores
            length_list = len(new_list)
            for i in new_list:
                sum += i
            average_score = sum / length_list
            # round_avg = round(average_score, 3)
            # print(f"{x:#.3g}")
            return('{:.2f}'.format(average_score))




if __name__ == "__main__":
    sample = {"eric": [20, 30, 40], "sam": [30, 30, 10, 30]}

    print(avg_dict(sample, 'eric'))
    print(avg_dict(sample, 'sam'))
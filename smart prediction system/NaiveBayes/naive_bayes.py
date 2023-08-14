import numpy as np
import pandas as pd




def check_datatype(data_columns,dataset):
        for column in data_columns:
                if(dataset[column].dtype != 'O'):
                        dataset[column] = dataset[column].astype('string')




def attribute_val(dataset,data_row,data_col):
    # step1 - define frequency table values

    attribute_values = [[] for i in range(data_col-1)]
    for j in range(data_col-1):
        values = set()
        for i in range(data_row):
            values.add(dataset[i][j])
        for val in values:
            attribute_values[j].append(val)
    # print(attribute_values)
    return attribute_values
    
    
def prediction_class(dataset,data_row,data_col,new_input):
    copy_of_attribute_values = attribute_val(dataset,data_row,data_col)
    label_val = []
    for  row in range(data_row):
        label_val.append(dataset[row][data_col-1])
    # print(label_val)

    label_category = set(label_val)
    list_label_category = list(label_category)

    cnt_category = [[0]for size in range(len(label_category))]
    for row in range(data_row):
        for category in label_category:
            if(category == dataset[row][data_col-1]):
                cnt_category[list(label_category).index(category)][0]+=1

    
    index_of_categories = []
    for val in label_category:
        index_of_categories.append(list_label_category.index(val))

   

    occurence = []

    for col in range(data_col-1):
        att_list = []
        for att_val in copy_of_attribute_values[col]:
            result = [[0]for size in range(len(list_label_category))]
            for row in range(data_row):
                if (dataset[row][col] == att_val):
                    for labels in list_label_category:
                        if(labels == dataset[row][data_col-1]):
                            result[list_label_category.index(labels)][0]+=1
        

            att_list.append(result)
        occurence.append(att_list)

    
    # step2 - define likelihood table values
    likelihood_val1 = []
    for a in range(len(occurence)):
        likelihood_val2 = []
        for b in range(len(occurence[a])):
            likelihood_val3 = []
            for c in range(len(occurence[a][b])):
                likelihood_val4 = []
                for d in range(len(occurence[a][b][c])):
                    likelihood_val4.append(occurence[a][b][c][d]/cnt_category[c][d])
                likelihood_val3.append(likelihood_val4)
            likelihood_val2.append(likelihood_val3)
        likelihood_val1.append(likelihood_val2)



    # step3 - take input from dataset or own
    category_prob = []
    for i in range(data_col-1):
        mid_prob = []
        input_val = new_input[i]
        for att_val in copy_of_attribute_values[i]:
            if(input_val == att_val):
                y = copy_of_attribute_values[i].index(att_val)
                prob = [[0]for j in range(len(label_category))]
                for label_val in label_category:
                    z = list(label_category).index(label_val)
                    prob[z][0] = likelihood_val1[i][y][z][0] 
                mid_prob.append(prob)
        category_prob.append(mid_prob)



    # step4 - calculate probabiliteis with respect categories in label column
    prob1 = [[1]for m in range(len(label_category))]
    for n in range(data_col-1):
        input_val = new_input[n]
        for att_val in copy_of_attribute_values[i]:
            if(input_val == att_val):
                for i in range(len(category_prob)):
                    for j in range(len(category_prob[i])):
                        for k in range(len(category_prob[i][j])):
                            for l in range(len(category_prob[i][j][k])):
                                prob1[k][l] = (prob1[k][l] * category_prob[i][j][k][l]) 
            
    
    
    prob2 = [[1]for m in range(len(label_category))]
    for i in range(len(prob1)):
        for j in range(len(prob1[i])):
            prob2[i][j] = prob1[i][j] * cnt_category[i][j]/data_row
        
    # step5 - check probabiliteis of category and decide output or predict output
    output = list_label_category[prob2.index(max(prob2))]
    return output
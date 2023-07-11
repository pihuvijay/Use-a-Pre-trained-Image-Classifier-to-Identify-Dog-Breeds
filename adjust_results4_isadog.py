#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Pihu Vijawargiya
# DATE CREATED:03/07/23                        
# REVISED DATE: 
# PURPOSE: Function that adjusts the results dictionary to indicate whether the pet image label is of a dog or not and whether the  classifier image label is of a dog. These labels from pet images and classifier are in the dognames txt file. Reccomend : read al dog names in dognames.txt into a dictionary using key- value pair, key is the dogname. If label is in the dictionary/list of dog names then it is a dog

#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.

#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 

#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    dognames_dic = dict()
    
    #opens dogfile file in read mode and parses through each line and enters into a data structure
    with open(dogfile, "r") as infile:
        line = infile.readline()
    # creates a while loop which loops until the line is empty (reaches end of file)
        while line != "":
            
    # TODO: 4a. REPLACE pass with CODE to remove the newline character
            #           from the variable line  
            #
            # Process line by striping newline from line
            line = line.rstrip()
            if line in dognames_dic:
                None
            else:
                dognames_dic[line] = 1
                
            line = infile.readline()    

        # Check to see if results_dic items are dogs
        for key in results_dic:
            
            
            if results_dic[key][0] in dognames_dic:
                
                
                if results_dic[key][1] in dognames_dic:
                    results_dic[key].extend((1, 1))
                else:
                    results_dic[key].extend((1,0))
                    
                    
            else:
                if results_dic[key][1] in dognames_dic:
                    results_dic[key].extend((0,1))
                else:
                    results_dic[key].extend((0,0))
   

# import statements
import re
from collections import defaultdict

# input file name to test
print('Which text file do you want to use for the puzzle? ', end='')
name_of_file = input()

# variables
contents = ''
name_of_sirs = set()
list_solution = []
truth_table = []
dict_name_quote = defaultdict(list)
person_in_quote = 0
type_quote = 1
type_person = 2
final_solution = []
# making data structure
dict_data_structure = {}
list_index_of_sirs_US = []
dict_knight_knave = {1: 'Knight', 0: 'Knave'}


# func to add names to list
def add_name_of_sir_set(list_of_names_param):
    for name_in_list in list_of_names_param:
        name_of_sirs.add(name_in_list)


# read from file
f = open(name_of_file, 'r')
if f.mode == 'r':
    contents = f.read()
f.close()

# remove next line ie \n from sentences
removed_next_line_contents = contents.translate({ord(c): ' ' for c in '\n'})

# find all the sentences
list_of_sentences = re.findall('\"*[A-Za-z,\": ]*[.?!]\"{0,1}', removed_next_line_contents)


# for each sentence find Sir names
for sentence in list_of_sentences:
    if 'Sir ' in sentence:
        name = re.findall('Sir\\s([A-Z][a-z]+)', sentence)
        add_name_of_sir_set(name)
    if 'Sirs ' in sentence:
        names = re.split('Sirs ', sentence)[1]
        list_of_names = re.findall('[A-Z][a-z]+', names)
        add_name_of_sir_set(list_of_names)

# check for knight and knave pollution
name_of_sirs.discard('Knight')
name_of_sirs.discard('Knights')
name_of_sirs.discard('Knaves')
name_of_sirs.discard('Knave')

number_of_sir = len(name_of_sirs)

# print Sirs
print('The Sirs are: ', end='')
counter = 1
for name in sorted(name_of_sirs):
    if number_of_sir == 1:
        print(name)
    elif number_of_sir >= 2:
        if counter != number_of_sir:
            print(name, end=' ')
            counter += 1
        elif counter == number_of_sir:
            print(name)


# if the sentence has "" save it as a key and value
for sentence in list_of_sentences:
    if '"' in sentence:
        quote = re.findall('"([^"]*)"', sentence)
        new_sentence = sentence.replace(quote[0], '')
        name = re.findall('Sir\\s([A-Z][a-z]+)', new_sentence)
        dict_name_quote[name[0]] += quote


def add_val_to_list_val(_list_person, _val, person_binary):
    return_list = list()
    return_list.append(_list_person)
    return_list.append(_val)
    return_list.append(person_binary)
    return return_list


list_from_set = list(sorted(name_of_sirs))
for n in list_from_set:
    list_index_of_sirs_US.append(list_from_set.index(n))

Knave = 0
Knight = 1

for name, quotes in dict_name_quote.items():
    list_val = []  # can have multiple quotes by the same person
    for quote in quotes:
        list_person = []
        if 'I ' in quote:
            new_quote = quote.replace('I ', 'Sir ' + name+' ')
            # find all Sir in quote
            names = re.findall('Sir\\s([A-Z][a-z]+)', new_quote)
            for n in names:
                list_person.append(list_from_set.index(n))
            # at least I
            if ' least ' in new_quote:
                if 'Knight' in new_quote:
                    if ' us ' in new_quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'least', Knight))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'least', Knight))
                if 'Knave' in new_quote:
                    if ' us ' in new_quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'least', Knave))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'least', Knave))

            # most I
            elif ' most ' in new_quote:
                if 'Knight' in new_quote:
                    if ' us ' in new_quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'most', Knight))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'most', Knight))
                if 'Knave' in new_quote:
                    if ' us ' in new_quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'most', Knave))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'most', Knave))

            # exactly I
            elif 'Exactly ' in new_quote or 'exactly' in new_quote:
                if 'Knight' in new_quote:
                    if ' us ' in new_quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'exactly', Knight))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'exactly', Knight))
                if 'Knave' in new_quote:
                    if ' us ' in new_quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'exactly', Knave))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'exactly', Knave))

            # all I
            elif 'all ' in new_quote or 'All ' in new_quote:
                if 'Knight' in new_quote:
                    list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'am', Knight))
                if 'Knave' in new_quote:
                    list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'am', Knave))

            # or Disjunction
            elif ' or ' in new_quote:
                if 'Knight' in new_quote:
                    list_val.append(add_val_to_list_val(list_person, 'least', Knight))
                if 'Knave' in new_quote:
                    list_val.append(add_val_to_list_val(list_person, 'least', Knave))

            # is am are I
            elif ' is ' in new_quote or ' am ' in new_quote or ' are ' in new_quote:
                if 'Knight' in new_quote:
                    list_val.append(add_val_to_list_val(list_person, 'am', Knight))
                if 'Knave' in new_quote:
                    list_val.append(add_val_to_list_val(list_person, 'am', Knave))
        else:
            names = re.findall('Sir\\s([A-Z][a-z]+)', quote)
            for n in names:
                list_person.append(list_from_set.index(n))
                # at least
            if ' least ' in quote:
                if 'Knight' in quote:
                    if 'us ' in quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'least', Knight))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'least', Knight))
                if 'Knave' in quote:
                    if 'us ' in quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'least', Knave))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'least', Knave))

            # most
            elif ' most ' in quote:
                if 'Knight' in quote:
                    if ' us ' in quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'most', Knight))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'most', Knight))
                if 'Knave' in quote:
                    if ' us ' in quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'most', Knave))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'most', Knave))

            # exactly
            elif 'Exactly' in quote or 'exactly ' in quote:
                if 'Knight' in quote:
                    if ' us ' in quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'exactly', Knight))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'exactly', Knight))
                if 'Knave' in quote:
                    if ' us ' in quote:
                        list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'exactly', Knave))
                    else:
                        list_val.append(add_val_to_list_val(list_person, 'exactly', Knave))

            # all
            elif 'All ' in quote or 'all ' in quote:
                if 'Knight' in quote:
                    list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'am', Knight))
                if 'Knave' in quote:
                    list_val.append(add_val_to_list_val(list_index_of_sirs_US, 'am', Knave))

            # or Disjunction
            elif ' or ' in quote:
                if 'Knight' in quote:
                    list_val.append(add_val_to_list_val(list_person, 'least', Knight))
                if 'Knave' in quote:
                    list_val.append(add_val_to_list_val(list_person, 'least', Knave))

            # is am are
            elif ' is ' in quote or ' am ' in quote or ' are ' in quote:
                if 'Knight' in quote:
                    list_val.append(add_val_to_list_val(list_person, 'am', Knight))
                if 'Knave' in quote:
                    list_val.append(add_val_to_list_val(list_person, 'am', Knave))

    dict_data_structure[list_from_set.index(name)] = list_val  # finally add items to the list

# print(dict_data_structure)

# generating binary numbers for truth table
for i in range(2 ** number_of_sir):
    bin_val = f'{i:0{number_of_sir}b}'
    t = ()
    for x in bin_val:
        t = t + (int(x),)
    truth_table.append(t)


# filling list_solution with name: value for representing knight and knave
for row in truth_table:
    dict_for_each_row = {}
    for name, val in zip(sorted(name_of_sirs), row):
        dict_for_each_row[name] = val
    list_solution.append(dict_for_each_row)


def cases(_dict):
    global truth_table
    for person, _quotes in _dict.items():
        for quote in _quotes:
            person_quote = quote[person_in_quote]
            type_of_quote = quote[type_quote]
            person_type = quote[type_person]
            other_persons = []
            if person in person_quote:
                # now remove person from person quote
                for p in person_quote:
                    if p != person:
                        other_persons.append(p)
                other_persons = sorted(other_persons)
            else:
                other_persons = person_quote

            # case 1 I am a knave, speaking person is Knave
            if person in person_quote and type_of_quote is 'am' and person_type is Knave and len(person_quote) == 1:
                return None

            # case 2 I am a Knight, return all possible solutions
            elif person in person_quote and type_of_quote is 'am' and person_type is Knight and len(person_quote) == 1:
                pass  # return truth_table

            # case 3 I and X / A and B are Knight
            elif len(person_quote) >= 2 and type_of_quote is 'am' and person_type is Knight and person in person_quote:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 1:  # speaking person should be one
                        for op in other_persons:  # check if any other is zero then remove
                            if tt in truth_table and tt[op] == 0:
                                removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when people are more than 2 and person type is a knight and speaking person is not in the sentence
            elif len(person_quote) >= 2 and type_of_quote is 'am' and person_type is Knight:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 1:
                        for op in other_persons:  # check if any other is zero then remove
                            if tt in truth_table and tt[op] == 0:
                                removing_elements.append(tt)
                    if tt[person] == 0:
                        c = 0
                        final_counter = len(person_quote)
                        for op in other_persons:  # check if any tuple has all 1's and remove
                            if tt in truth_table and tt[op] == 1:
                                c += 1
                                if c == final_counter:
                                    removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when X is a knight todo may create problem
            elif len(person_quote) == 1 and type_of_quote is 'am' and person_type is Knight and person not in person_quote:
                removing_elements = []
                for tt in truth_table:
                    for op in other_persons:
                        if tt[person] != tt[op]:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when At least one of us is a Knight ie I and B C are Knight todo check with atul truth table
            elif person in person_quote and type_of_quote is 'least' and person_type is Knight:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 0:
                        c = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c != final_counter:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when at least one of sir b and sir c is a knight
            elif person not in person_quote and type_of_quote is 'least' and person_type is Knight:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 1:
                        c = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c == final_counter:
                            removing_elements.append(tt)
                    elif tt[person] == 0:
                        c = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c != final_counter:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when exactly one us is a knight
            elif person in person_quote and type_of_quote is 'exactly' and person_type is Knight:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 0:
                        c0 = 0
                        c1 = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c0 += 1
                            elif tt[op] == 1:
                                c1 += 1
                        if final_counter == c0 or c1 > 1:
                            pass
                        else:
                            removing_elements.append(tt)
                    elif tt[person] == 1:
                        c = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c != final_counter:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when Exactly one of sir A and Sir B is a Knight
            elif person not in person_quote and type_of_quote is 'exactly' and person_type is Knight:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 0:
                        c0 = 0
                        c1 = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c0 += 1
                            elif tt[op] == 1:
                                c1 += 1
                        if final_counter == c0 or final_counter == c1:
                            pass
                        else:
                            removing_elements.append(tt)
                    elif tt[person] == 1:
                        c = 0
                        for op in other_persons:
                            if tt[op] == 1:
                                c += 1
                        if c != 1:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when At most one of us is a Knight
            elif person in person_quote and type_of_quote is 'most' and person_type is Knight:
                removing_elements = []
                pass
                for tt in truth_table:
                    if tt[person] == 0:
                        c = 0
                        for op in other_persons:
                            if tt[op] == 1:
                                c += 1
                        if c > 1:
                            pass
                        else:
                            removing_elements.append(tt)
                    elif tt[person] == 1:
                        c = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c == final_counter:
                            pass
                        else:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when At most sir B and Sir C is a Knight
            elif person not in person_quote and type_of_quote is 'most' and person_type is Knight:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 0:
                        c1 = 0
                        for op in other_persons:
                            if tt[op] == 1:
                                c1 += 1
                        if c1 > 1:
                            pass
                        else:
                            removing_elements.append(tt)
                    elif tt[person] == 1:
                        c0 = 0
                        c1 = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 1:
                                c1 += 1
                            if tt[op] == 0:
                                c0 += 1
                        if c1 == 1 or c0 == final_counter:
                            pass
                        else:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when Sir A, Sir B and Sir C are Knaves and speaker is A ie all of us are knave
            elif person in person_quote and type_of_quote is 'am' and person_type is Knave:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 1:
                        removing_elements.append(tt)
                    elif tt[person] == 0:
                        c = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c == final_counter:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when Sir B and Sir C are Knaves and speaker is not in spoken list
            elif person not in person_quote and type_of_quote is 'am' and person_type is Knave:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 0:
                        c = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c == final_counter:
                            removing_elements.append(tt)
                    elif tt[person] == 1:
                        c = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c != final_counter:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when At least one of us is a Knave
            elif person in person_quote and type_of_quote is 'least' and person_type is Knave:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 0:
                        removing_elements.append(tt)
                    elif tt[person] == 1:
                        c = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 1:
                                c += 1
                        if c == final_counter:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case when At least Sir B and Sir C is a Knave
            elif person not in person_quote and type_of_quote is 'least' and person_type is Knave:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 0:
                        c = 0
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c != 0:
                            removing_elements.append(tt)
                    elif tt[person_type] == 1:
                        c = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 1:
                                c += 1
                        if c == final_counter:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case Exactly one of us is a Knave
            elif person in person_quote and type_of_quote is 'exactly' and person_type is Knave:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 0:
                        c = 0
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c >= 1:
                            pass
                        else:
                            removing_elements.append(tt)
                    elif tt[person] == 1:
                        c = 0
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c != 1:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case Exactly Sir B and Sir C is a Knave said by Sir A
            elif person not in person_quote and type_of_quote is 'exactly' and person_type is Knave:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 0:
                        c = 0
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c == 1:
                            removing_elements.append(tt)
                    elif tt[person] == 1:
                        c = 0
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c != 1:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case At most one of us is a Knave
            elif person in person_quote and type_of_quote is 'most' and person_type is Knave:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 0:
                        c = 0
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c >= 1:
                            pass
                        else:
                            removing_elements.append(tt)
                    elif tt[person] == 1:
                        c = 0
                        c1 = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                            elif tt[op] == 1:
                                c1 += 1
                        if c != 1 and not c1 == final_counter:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))

            # case At most one of Sir C and Sir B is a Knave
            elif person not in person_quote and type_of_quote is 'most' and person_type is Knave:
                removing_elements = []
                for tt in truth_table:
                    if tt[person] == 0:
                        c = 0
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                        if c >= 2:
                            pass
                        else:
                            removing_elements.append(tt)
                    elif tt[person] == 1:
                        c = 0
                        c1 = 0
                        final_counter = len(other_persons)
                        for op in other_persons:
                            if tt[op] == 0:
                                c += 1
                            elif tt[op] == 1:
                                c1 += 1
                        if c == 1 or c1 == final_counter:
                            pass
                        else:
                            removing_elements.append(tt)
                truth_table = list(set(truth_table).difference(set(removing_elements)))
    return truth_table


print(dict_data_structure)
final = cases(dict_data_structure)
if final is None:
    print('There is no solution.')
else:
    if len(final) == 1:
        print('There is a unique solution:')
        for name, type_of_person in zip(list_from_set, final[0]):
            print(f'Sir {name} is a {dict_knight_knave[type_of_person]}.')
    elif len(final) >= 2:
        print(f'There are {len(final)} solutions.')

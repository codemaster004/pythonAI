import pandas as pd
import itertools
import operator
import numpy


class DecisionTree:
    label = ''
    model_data = None
    columns = None
    checking_notes = {}
    results = []
    tree = {}

    class CheckingNote:
        col_name = ''
        col_values = []
        computing = {}
        results = []
        gini_impurity = 1

        def __init__(self, col_name, col_values, results):
            self.col_name = col_name
            self.col_values = col_values
            self.results = results

            self.computing = {}
            for v in self.col_values:
                self.computing[v] = {r: 0 for r in results}
                self.computing[v]['cases'] = 0
            self.computing['all_cases'] = 0

        def set_value(self, value, result, number):
            self.computing[value][result] = number
            self.computing[value]['cases'] += number
            self.computing[value]['name'] = value
            self.computing['all_cases'] += number

        def __calc_p__(self, numbers):
            result = [n / numpy.sum(numbers) for n in numbers]
            return result

        def calc_impurity(self):
            impurities = []
            for v in self.col_values:
                leaf_numbers = [self.computing[v][r] for r in self.results]
                probabilities = self.__calc_p__(leaf_numbers)
                impurity = 1 - probabilities[0] ** 2 - probabilities[1] ** 2
                self.computing[v]['impurity'] = impurity
                impurities.append((impurity, self.computing[v]['cases']))
            probabilities = self.__calc_p__([i[1] for i in impurities])
            gini = 0
            for i in range(len(probabilities)):
                gini += probabilities[i] * impurities[i][0]
            self.gini_impurity = gini

        def pick_value(self):
            print(self.computing.items())
            sorted_impurities = sorted(self.computing.items(), key=lambda obj: obj[1]['impurity'])

            # print(sorted_impurities)
            # print(sorted_impurities[0].name)

    class TreeNote:
        name = ''
        condition = ''
        note_type = ''

        def __init__(self, name, condition, note_type):
            self.name = name
            self.condition = condition
            self.note_type = note_type

    def __init__(self, label):
        self.label = label

    def __combinator_values__(self, values):
        combined = []
        for i in range(len(values) - 1):
            separator = '||'
            values_com = list(itertools.combinations(values, i + 1))
            for v_set in values_com:
                combined.append(separator.join(v_set))
        return combined

    def __create_condition__(self, value):
        const_part = '(self.model_data[col] == "'

        str_condition = ''
        for w in value.split('||'):
            str_condition += const_part
            str_condition += w
            str_condition += '")'
            if w != value.split('||')[-1]:
                str_condition += ' | '
        return str_condition

    def load_data(self, src):
        with open(src, newline='') as csv_file:
            df = pd.read_csv(csv_file, delimiter=';')
            self.model_data = df

            self.columns = set(df.columns)
            self.columns.remove(self.label)
            self.results = set(df[self.label])

    def find_note(self):
        for col in self.columns:
            values = set(self.model_data[col])
            values = self.__combinator_values__(values)
            self.checking_notes[col] = self.CheckingNote(col, values, self.results)
            for v in values:
                if '||' in v:
                    condition = self.__create_condition__(v)
                    filtered_by_value = self.model_data[eval(condition)]
                else:
                    filtered_by_value = self.model_data[self.model_data[col] == v]

                for r in self.results:
                    n = len(filtered_by_value[filtered_by_value[self.label] == r])
                    self.checking_notes[col].set_value(v, r, n)
        for col in self.columns:
            self.checking_notes[col].calc_impurity()
        sorted_impurities = sorted(self.checking_notes.values(), key=operator.attrgetter('gini_impurity'))
        picked_note = sorted_impurities[0]
        picked_note.pick_value()
        self.tree['self'] = self.TreeNote(picked_note.col_name, '', '')


myTree = DecisionTree('result')
myTree.load_data('../data/DataTest.csv')
myTree.find_note()

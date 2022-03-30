from datetime import date

def Get_TimeTable():
	file = open('table.txt', encoding='utf-8')

	weeks = []

	for week_i in range(2):
		weeks.append([])

		for day_i in range(6):
			weeks[week_i].append([])
			
			# Scip void
			file.readline()
			file.readline()

			for subj_i in range(6):
				subj_n = file.readline().replace('\n', '')
				weeks[week_i][day_i].append(subj_n)

				# Scip void
				file.readline()
				
			# Scip void
			file.readline()
			file.readline()

	return weeks

def Get_Data(subject):
	_none_subject = '───'
	if subject == '_':
		return _none_subject, _none_subject
	subject_a = subject_b = _none_subject

	is_tag = False

	_all = 0
	_first = 1
	_second = 2

	group_tag = _all

	for c in subject:
		if (c == '<'):
			is_tag = True
			continue
		if is_tag:
			if (c == '/'):
				group_tag = _all
				continue
			elif c == '1':
				group_tag = _first
			elif c == '2':
				group_tag = _second
			elif c == '>':
				is_tag = False
			continue

		if group_tag == _first:
			if subject_a == _none_subject:
				subject_a = c
			else:
				subject_a += c

		elif group_tag == _second:
			if subject_b == _none_subject:
				subject_b = c
			else:
				subject_b += c

		elif group_tag == _all:
			if subject_a == _none_subject:
				subject_a = subject_b = c
			else:
				subject_a += c
				subject_b += c
				
	return subject_a, subject_b


if __name__ == '__main__':
	time_table = Get_TimeTable()
	with open('index.html', 'w', encoding='utf-8') as result_file:
		result = open('template.html', encoding='utf-8').read()
		for week_i in range(2):
			for day_i in range(6):
				for subj_i in range(6):
					key = f'{week_i+1}{day_i+1}{subj_i+1}'
					key_a, key_b = f'%1{key}%', f'%2{key}%'
					subject = time_table[week_i][day_i][subj_i]



					data_a, data_b = Get_Data(subject)
					result = result.replace(key_a, data_a).replace(key_b, data_b).replace('%RefreshData%', date.today().strftime("%d.%m.%Y"))

		result_file.write(result)
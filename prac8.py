sublist = ['english','maths','history']
sub2 = 'science'
sublist.append(sub2)
print(sublist)

sublist.insert(0,'hindi')
print(sublist)

sub2list = ['marathi','geography']
sublist.extend(sub2list)
print(sublist)

sublist.remove('maths')
print(sublist)
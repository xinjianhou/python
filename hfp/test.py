Python 3.6.3 (default, Oct  4 2017, 06:09:38) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.37)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
python3
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    python3
NameError: name 'python3' is not defined
>>> if 2>1
SyntaxError: invalid syntax
>>> if 2>1;
SyntaxError: invalid syntax
>>> if 2>1:
	print("haha");

	
haha
>>> movies=["The holy grail","hally potter","god of war"];
>>> print(movies);
['The holy grail', 'hally potter', 'god of war']
>>> print（movies[1]);
SyntaxError: invalid character in identifier
>>> print(movies[1]);
hally potter
>>> movies.append("death or live");
>>> print(movies);
['The holy grail', 'hally potter', 'god of war', 'death or live']
>>> print(len(movies));
4
>>> movies.pop();
'death or live'
>>> print(movies);
['The holy grail', 'hally potter', 'god of war']
>>> movies.append(['haha','red font']);
>>> print(movies);
['The holy grail', 'hally potter', 'god of war', ['haha', 'red font']]
>>> movies.append(["haha","red font"]);
>>> print(movies);
['The holy grail', 'hally potter', 'god of war', ['haha', 'red font'], ['haha', 'red font']]
>>> movies.extend(['nihao','beiying']);
>>> print(movies);
['The holy grail', 'hally potter', 'god of war', ['haha', 'red font'], ['haha', 'red font'], 'nihao', 'beiying']
>>> movies.remove('hehe');
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    movies.remove('hehe');
ValueError: list.remove(x): x not in list
>>> movies.remove('nihao');
>>> print(movies);
['The holy grail', 'hally potter', 'god of war', ['haha', 'red font'], ['haha', 'red font'], 'beiying']
>>> movies.insert(1,'hehe');
>>> print(movies);
['The holy grail', 'hehe', 'hally potter', 'god of war', ['haha', 'red font'], ['haha', 'red font'], 'beiying']
>>> movies=["The holy grail","hally potter","god of war"];
>>> print(movies);
['The holy grail', 'hally potter', 'god of war']
>>> movies.insert(1,1987)
>>> movies.insert(3,2001)
>>> movies.insert(5,1864);
>>> print(movies);
['The holy grail', 1987, 'hally potter', 2001, 'god of war', 1864]
>>> for per_movie in movies:
	print(per_movie);

	
The holy grail
1987
hally potter
2001
god of war
1864
>>> count = 0
>>> while count < len(movies):
	print(movies[count])
	count++;
	
SyntaxError: invalid syntax
>>> while count < len(movies):
	print(movies[count])
	count++
	
SyntaxError: invalid syntax
>>> while count < len(movies):
	print(movies[count])
	count = count+1;

	
The holy grail
1987
hally potter
2001
god of war
1864
>>> movies.append(['detaoil','nihao']);
>>> print(movies);
['The holy grail', 1987, 'hally potter', 2001, 'god of war', 1864, ['detaoil', 'nihao']]
>>> for per in movies:
	if isinstance(per,list):
		for per_i in per:
			print(per_i)

			
detaoil
nihao
>>> for per in movies:
	if isinstance(per,list):
		for per_i in per:
			print(per_i)
	else:
		print(per)

		
The holy grail
1987
hally potter
2001
god of war
1864
detaoil
nihao
>>> movies=['hally poter','red font','walking dead']
>>> movies.append(['hello world','heheda',[12,23,23,45,'nihao']]);
>>> print(movies);
['hally poter', 'red font', 'walking dead', ['hello world', 'heheda', [12, 23, 23, 45, 'nihao']]]
>>> def print_lol(the_list):
	for iteam in the_list:
		if isinstance(iteam,list):
			print_lol(iteam);
		else:
			print(iteam);

			
>>> print_lol(movies);
hally poter
red font
walking dead
hello world
heheda
12
23
23
45
nihao
>>> '''die dai '''
'die dai '
>>> 

#!/usr/bin/python
import unittest
import ropes
import random
#from test import test_support, string_tests

#TODO: Make these unit tests more torturous

#para1='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec tortor elit, tincidunt a, sodales vitae, aliquet vel, risus. Cras fringilla dapibus enim. Morbi ultrices pulvinar orci. Praesent placerat massa a nulla. Integer blandit tincidunt lorem. Proin imperdiet convallis dolor. Aliquam ac nisi. Morbi dapibus luctus risus. Pellentesque viverra, arcu at mattis tempor, nisl leo molestie sem, in auctor mi augue a nisl. Donec metus elit, egestas vel, convallis vel, condimentum a, mi. Suspendisse ultricies pede in justo. Mauris at justo.'
para1='hello'*1024
para2='Cras ac felis. Proin eget metus. Nullam tristique tristique leo. Integer ullamcorper viverra diam. Sed faucibus fringilla enim. Fusce augue. Nunc a dolor. Sed rhoncus ligula a orci. Integer diam felis, semper at, tempor at, dapibus id, orci. Nam eget arcu id lorem congue vehicula. Proin facilisis libero eget neque. Sed congue lobortis nunc.'
para3='In sapien. Fusce viverra lectus in tortor. Nam lobortis massa quis pede. Praesent et est vel purus consequat placerat. In tellus ligula, viverra nec, mattis eu, pretium ac, nulla. Etiam ultrices nisi vel sapien. Quisque leo mauris, vehicula et, condimentum tristique, luctus a, magna. Donec id ante. Proin felis urna, fringilla ut, ullamcorper sed, molestie at, arcu. Curabitur est odio, iaculis ac, dapibus at, ultrices id, risus. Nulla accumsan. Morbi sagittis porta nibh.'
para4='Proin molestie fermentum diam. Nullam imperdiet. Mauris felis. Donec ut quam. Suspendisse potenti. Sed sapien nunc, pulvinar eget, feugiat et, imperdiet eget, sem. Vivamus porttitor eros aliquam ligula. Suspendisse ultrices consectetuer nulla. Sed est. Donec sem dolor, facilisis a, lacinia eget, lobortis nonummy, ipsum. Nulla facilisi. Donec et sem. Fusce in nibh a nunc luctus pharetra. Pellentesque lorem metus, vulputate aliquet, elementum non, egestas a, tortor.'
para5='Curabitur ligula mi, varius aliquet, consectetuer non, blandit et, leo. Nulla egestas tristique nibh. In ultrices accumsan magna. Aenean non augue. Fusce nonummy turpis sit amet est. Integer aliquet vulputate diam. Vivamus urna neque, vestibulum id, tincidunt sed, molestie vitae, nisi. Phasellus nonummy urna ac nibh. Phasellus in arcu sit amet metus consequat molestie. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Cras lacinia dui ac lorem. Nam in leo sed justo mattis ultricies. Proin vitae urna. Quisque commodo tincidunt lacus. Mauris luctus felis a mi. Vestibulum posuere. Duis vel metus malesuada velit laoreet porttitor. Proin suscipit viverra diam. Morbi fringilla vestibulum eros.'

class TestRopes(unittest.TestCase):
    def testAppends(self):
        r1=ropes.Rope()
        r2=ropes.Rope()
        r2+=ropes.Rope(para4)
        r2+=ropes.Rope(para5)
        r1+=ropes.Rope(para1)
        r1+=ropes.Rope(para2)
        r1+=ropes.Rope(para3)
        r1+=r2
        self.assertEqual(str(r1),para1+para2+para3+para4+para5);

    def testBalance(self):
        r1=ropes.Rope()
        r1+=ropes.Rope(para1)
        r1+=ropes.Rope(para2)
        r1+=ropes.Rope(para3)
        r1+=ropes.Rope(para4)
        r1+=ropes.Rope(para5)
        r1.balance()
        self.assertEqual(str(r1),para1+para2+para3+para4+para5);

    def testRepetition(self):
        r1=ropes.Rope('hello')
        r1*=100
        self.assertEqual(str(r1),'hello'*100)

    def testLength(self):
        r1=ropes.Rope('hell')
        r1+=ropes.Rope('o, w')
        r1+=ropes.Rope('orld')
        self.assertEqual(len(r1), 12)

    def testLength(self):
        r1=ropes.Rope('hello')
        r1*=100
        self.assertEqual(len(r1), 500)

    def testSlicing(self):
        r1=ropes.Rope(para1)
        r1+=ropes.Rope(para2)
        s1=para1+para2
        start=random.randint(0, len(r1)-1)
        end=random.randint(start+1, len(r1))
        self.assertEqual(str(r1[start:end]), s1[start:end])

    def testComparisons(self):
        r1=ropes.Rope(para1+para2)
        r2=ropes.Rope(para1)
        r2+=ropes.Rope(para2)
        self.assertEqual(r1, r2)
        r1=ropes.Rope('hello')*3
        r2=ropes.Rope('hello')*2
        r2+=ropes.Rope('hello')
        self.assertEqual(r1, r2)
        
    def testHashing(self):
        r1 = ropes.Rope(para1 + para2 + para3)
        r2 = ropes.Rope(para1)
        r2 += ropes.Rope(para2)
        r2 = r2 + ropes.Rope(para3)
        self.assertEqual(hash(r1), hash(r2))

    def testIteration(self):
        r1 = ropes.Rope(para1 + para2 + para3)
        r2 = ropes.Rope('')
        for c in r1:
            r2 += ropes.Rope(c)
        self.assertEqual(str(r1), str(r2))

if __name__=="__main__":
    unittest.main()

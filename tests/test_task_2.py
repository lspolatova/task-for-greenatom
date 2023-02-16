from unittest import TestCase
from task_2 import create_handlers, execute_handlers


class Test(TestCase):
    def test_create_handlers(self):
        def callback(step):
            return step
        handlers = create_handlers(callback)
        self.assertEqual([handlers[i]() for i in range(5)], [0, 1, 2, 3, 4])


class Test(TestCase):
    def test_execute_handlers(self):
        current = ''

        def loading(step):
            nonlocal current
            current = f'{current}Step {step} done\n'
        handlers = create_handlers(loading)
        execute_handlers(handlers)
        self.assertEqual(current, 'Step 0 done\nStep 1 done\nStep 2 done\nStep 3 done\nStep 4 done\n')

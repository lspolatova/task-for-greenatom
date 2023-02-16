from typing import Any, Callable, List


def create_handlers(callback: Callable[[int], Any]) -> List[Callable[[int], Any]]:
    handlers = []
    for step in range(5):
        handlers.append(lambda step_loc=step: callback(step_loc))
    return handlers


def execute_handlers(handlers: List[Callable[[int], Any]]) -> None:
    for handler in handlers:
        handler()

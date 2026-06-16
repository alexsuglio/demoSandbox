def greet(name: str) -> str:
	return f"Hello, {name}!"


def add_numbers(a: float, b: float) -> float:
	return a + b


def is_even(value: int) -> bool:
	return value % 2 == 0


def format_user(user_id: int, username: str, active: bool = True) -> dict:
	return {
		"id": user_id,
		"username": username,
		"active": active,
	}

def get_dummy_items(count: int = 3) -> list[str]:
	return [f"item_{i + 1}" for i in range(count)]


if __name__ == "__main__":
	print(greet("Alex"))
	print(add_numbers(4, 7))
	print(is_even(10))
	print(format_user(1, "demo_user"))
	print(get_dummy_items())

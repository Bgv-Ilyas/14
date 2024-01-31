def create_html_list(strings):
    def inner_function():
        result = "<ol>\n"
        for string in strings:
            result += f"<li>{string}</li>\n"
        result += "</ol>"
        return result

    return inner_function

# Пример использования замыкания
my_list = ["строка_1", "строка_2", "строка_3"]
html_list_generator = create_html_list(my_list)
result_html = html_list_generator()

print(result_html)

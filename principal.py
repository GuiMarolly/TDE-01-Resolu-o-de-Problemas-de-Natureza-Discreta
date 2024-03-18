def process_input_file(input_file):
    with open(input_file, 'r') as file:  #'R' pra ler o arquivo
        lines = file.readlines() # Pra ler todas as linhas
        num_operations = int(lines[0].strip())
        operations = []              #Começa vazia pra colocar as coisas
        for i in range(1, len(lines), 3):
            operation = {}
            operation['type'] = lines[i].strip()
            operation['set1'] = [x.strip() for x in lines[i+1].split(',')]
            operation['set2'] = [x.strip() for x in lines[i+2].split(',')]
            operations.append(operation)
    return num_operations, operations

def perform_union(set1, set2):
    return set(set1) | set(set2)

def perform_intersection(set1, set2):
    return set(set1) & set(set2)

def perform_difference(set1, set2):
    return set(set1) - set(set2)

def perform_cartesian_product(set1, set2):
    return [(x, y) for x in set1 for y in set2]

def process_operations(num_operations, operations):
    results = []
    for operation in operations:
        op_type = operation['type']
        set1 = operation['set1']
        set2 = operation['set2']
        result_set = None
        if op_type == 'U':
            result_set = perform_union(set1, set2)
        elif op_type == 'I':
            result_set = perform_intersection(set1, set2)
        elif op_type == 'D':
            result_set = perform_difference(set1, set2)
        elif op_type == 'C':
            result_set = perform_cartesian_product(set1, set2)
        results.append((op_type, set1, set2, result_set))
    return results

def format_output(results):
    for op_type, set1, set2, result_set in results:
        print(f"{op_type}:", end=" ")
        if op_type == 'C':
            result_str = ', '.join([f"({x[0]}, {x[1]})" for x in result_set])
            print(f"conjunto 1 {{{', '.join(set1)}}}, conjunto 2 {{{', '.join(set2)}}}. Resultado: {{{result_str}}}")
        else:
            print(f"conjunto 1 {{{', '.join(set1)}}}, conjunto 2 {{{', '.join(set2)}}}. Resultado: {{{', '.join(result_set)}}}")

def main():
    input_file = "input.txt"  
    num_operations, operations = process_input_file(input_file)
    results = process_operations(num_operations, operations)
    format_output(results)

if __name__ == "__main__":
    main()

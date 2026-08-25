def describe_person(*args, **kwargs):
    print(args)
    print(kwargs)

args = list(input("Enter: ").split())
# kwargs = input("Enter key value pairs: ").split()
describe_person(args, yoe=7, role="engineer")
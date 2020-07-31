'''
"path" = "/foo/../test/../test/../foo//bar/./baz"
expected = "/foo/bar/baz"


"path": "../../../this////one/./../../is/../../going/../../to/be/./././../../../just/eight/double/dots/../../../../../.."
expected = "../../../../../../../.."

'''

# Version 1
# Filling answer array from the beginning. Pop value, if we meet "..".
# Add "" 1st elem if 1st is "/". To handle relative path with "../../........."

# Version 2

def shortenPath(path):
    skip = ['.', '']
    main_stack = path.split('/')
    short_path = []
    dots_stack = []

    for i in range(len(main_stack)):
        symbol = main_stack.pop()
        if symbol not in skip:
            if symbol != '..':
                if len(dots_stack) == 0:
                    short_path.append(symbol)
                else:
                    dots_stack.pop()
            else:
                dots_stack.append(symbol)

    answer = '/' if path[0] == '/' else '/'.join(dots_stack)
    if len(dots_stack) != 0 and len(short_path) != 0 and path[0] != '/':
        answer += '/'
    answer += '/'.join(reversed(short_path))

    return answer
			

pluck = lambda dict, *args: (dict[arg] if arg in dict else None for arg in args)

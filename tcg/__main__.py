def main():
    # from hello_world import HelloWorld
    import argparse

    args_parser = argparse.ArgumentParser()

    # Add args as required

    args_parser.add_argument("-t", "--text", required=True, default="Hello World")

    # Make boolean
    def make_bool(in_str):
        bools_dict = {"True":True, "TRUE":True,1:True,"1":True,
                      "T":True, "False": False, "F": False, "0": False,
                      "FALSE": False, 0: False}
        if in_str:
            return bools_dict[in_str]


    use_arguments = args_parser.parse_args()


    try:
        pass
    except Exception:
        # TODO: Use specific Exception
        raise
    else:
        print("Thank you for using tcg, please provide feedback at https://github.com/Nelson-Gon/tcg")


if __name__=="__main__":
    main()



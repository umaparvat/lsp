class FoodProcessor:

    def chop(self, item):
        # code logic to chop the items
        print(f"chopping the {item}")

    def mince(self, item):
        # code logic to mince the items
        print(f"Minicing the {item}")


class Mincer(FoodProcessor):

    def chop(self, item):
        raise NotImplementedError

    def mince(self, item):
        super().mince(item)


# client code
class Processor:

    def execute(self, fp: [FoodProcessor], item):
        for each_fp_processor in fp:
            each_fp_processor.chop(item)  # violates lsp


if __name__ == "__main__":
    fp_ins = FoodProcessor()
    mn_ins = Mincer()
    prc_ins = Processor()
    prc_ins.execute([fp_ins, mn_ins], "carrots")


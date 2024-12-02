from flyer import Flyer

def main():
    # Example usage
    flyer1 = Flyer("Landscape", "Discount Offer", "Red")
    flyer2 = flyer1.clone()  # Uses deepcopy and then clone_marketing_material() for Flyer
    flyer2.print_material()

if __name__ == "__main__":
    main()
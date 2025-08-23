from src.crew import aidea_link_crew

def main():
    """Main function to run the AIdeaLink crew."""
    print("Please enter the founder profile (e.g., 'AI startup, $500k seed'): ")
    founder_profile = input()
    if founder_profile:
        result = aidea_link_crew.kickoff(inputs={'founder_profile': founder_profile})
        print("\n\nFinal Report:")
        print(result)

if __name__ == "__main__":
    main()

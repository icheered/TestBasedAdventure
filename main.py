from utilities import get_story, extract_options, run_story

def main():
    story = get_story('story.txt')
    story_dict = extract_options(story)
    run_story(story_dict)

if __name__ == "__main__":
    main()
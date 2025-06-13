# app.py
import argparse
from tasks.summarizer      import summarize
from tasks.qa              import answer
from tasks.transcription   import transcribe
from tasks.image_caption   import caption_image

def main():
    p = argparse.ArgumentParser("AI Toolkit")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("summarize");    s.add_argument("file")
    q = sub.add_parser("qa");           q.add_argument("question"); q.add_argument("file")
    t = sub.add_parser("transcribe");   t.add_argument("audio")
    c = sub.add_parser("caption");      c.add_argument("image")

    args = p.parse_args()
    if args.cmd == "summarize":
        txt = open(args.file, encoding="utf-8").read()
        print(summarize(txt))
    elif args.cmd == "qa":
        ctx = open(args.file, encoding="utf-8").read()
        print(answer(args.question, ctx))
    elif args.cmd == "transcribe":
        print(transcribe(args.audio))
    elif args.cmd == "caption":
        print(caption_image(args.image))

if __name__ == "__main__":
    main()

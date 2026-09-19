# Python mini-projects

Things I built while learning Python — some games, a scraper, and a bit of computer
vision.

## Computer vision

Three scripts built on YOLOv8. `object_detection_yolo.py` annotates a still image,
`yolo_webcam.py` does the same live from the webcam, and `car_counter.py` counts
vehicles crossing a line in a video — YOLO finds them, a mask ignores the parts of the
frame I don't care about, and SORT tracking keeps the same ID on a car between frames
so nothing gets counted twice.

## Games

- **Tic-tac-toe** — Pygame, with a minimax opponent you can't beat
- **Minesweeper** — recursive flood fill to open the empty regions
- **Chess**, **Snake** and **Pong** — terminal and turtle versions, written to
  practise game loops and collision handling

## Scraping

`WebScraping_YallaKoora_BS4.py` pulls football match data with requests and
BeautifulSoup and writes it out to CSV.

## Running them

The games need nothing but the standard library, apart from tic-tac-toe (Pygame and
NumPy). For the rest:

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

The detection scripts expect the YOLO weights in `Yolo-Weights/` one level up —
Ultralytics downloads them on first run — and the car counter also needs a `video.mp4`
and a `mask.png`. None of those are in the repo.

## Credit

`object-detection/SORT.py` isn't mine. It's Alex Bewley's
[SORT tracker](https://github.com/abewley/sort), GPL-3.0, included unchanged with its
original header. Everything else here I wrote.

---

**Salmen Hammami** · [GitHub](https://github.com/salmenhammami) · [LinkedIn](https://www.linkedin.com/in/salmenhammami/)

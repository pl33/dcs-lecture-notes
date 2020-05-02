
BUILD_DIR = build

LATEXMK = latexmk -pdf -silent -synctex=1
LATEXMK_PVC = $(LATEXMK) -pvc

ALL_CHAPTERS = $(BUILD_DIR)/chapter00.pdf $(BUILD_DIR)/chapter01.pdf $(BUILD_DIR)/chapter02.pdf
ALL_EXERCISES = $(BUILD_DIR)/exercise00.pdf
COMMON_DEPS = common/settings.tex common/titlepage.tex common/acronym.tex common/imprint.tex DCS.bib

all: chapters exercises complete

.PHONY: chapters
chapters: $(ALL_CHAPTERS)

.PHONY: exercises
exercises: $(ALL_EXERCISES)

.PHONY: complete
complete: $(BUILD_DIR)/DCS.pdf

clean:
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; rm -f *.aux *.fdb_latexmk *.fls *.lof *.log *.lot *.pdf *.synctex.gz

$(BUILD_DIR)/DCS.pdf: main/DCS.tex $(COMMON_DEPS) */*.tex
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; $(LATEXMK) ../$<

$(BUILD_DIR)/%.pdf: main/%.tex $(COMMON_DEPS) %/*.tex
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; $(LATEXMK) ../$<

%-watch: main/%.tex
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; $(LATEXMK_PVC) ../$<

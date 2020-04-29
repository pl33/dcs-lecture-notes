
BUILD_DIR = build

LATEXMK = latexmk -pdf -silent -synctex=1
LATEXMK_PVC = $(LATEXMK) -pvc

ALL_TARGETS = $(BUILD_DIR)/chapter00.pdf $(BUILD_DIR)/chapter01.pdf
COMMON_DEPS = common/settings.tex common/titlepage.tex common/acronym.tex common/imprint.tex

all: $(ALL_TARGETS)

clean:
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; rm -f *.aux *.fdb_latexmk *.fls *.lof *.log *.lot *.pdf *.synctex.gz

$(BUILD_DIR)/%.pdf: main/%.tex $(COMMON_DEPS) %/*.tex
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; $(LATEXMK) ../$<

%-watch: main/%.tex
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; $(LATEXMK_PVC) ../$<

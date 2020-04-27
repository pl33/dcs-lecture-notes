
BUILD_DIR = build

LATEXMK = latexmk -pdf -silent -synctex=1
LATEXMK_PVC = $(LATEXMK) -pvc

ALL_TARGETS = $(BUILD_DIR)/chapter01.pdf

all: $(ALL_TARGETS)

clean:
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; rm -f *.aux *.fdb_latexmk *.fls *.lof *.log *.lot *.pdf *.synctex.gz

$(BUILD_DIR)/%.pdf: main/%.tex
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; $(LATEXMK) ../$<

%-watch: main/%.tex
	mkdir -p $(BUILD_DIR)
	cd $(BUILD_DIR) ; $(LATEXMK_PVC) ../$<

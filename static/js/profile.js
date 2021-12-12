

function createRemoveFormBoxes(addRemoveLoc, totalLocId, addButton, arrayClass, removeButton, inputOrTextarea, totalItemsLocation, countStepsIngreds) {
    let arrayIngredientLength = document.querySelectorAll(countStepsIngreds).length; // Counts number of present boxes
    let totalLoc = document.getElementById(totalLocId).getElementsByTagName("span")[0]; // User visible box number counter location
    let addRemoveLocation = document.getElementsByClassName(addRemoveLoc)[0]; // Parent of all boxes to be added/removed

    // Updates box counters for form input and user experience
    function updateBoxCounters() {
        totalLoc.textContent = arrayIngredientLength;
        document.getElementById(totalItemsLocation).value = arrayIngredientLength;
    }
    // Initial update for counters
    updateBoxCounters();

    // Creates additional boxes when add button is clicked
    document.querySelector(addButton).addEventListener("click", function() {

        console.log("I am here")

        // Updates, Increases counter for created box
        arrayIngredientLength++;
        updateBoxCounters();

        // Creation of elements and adding of content into new step/ingredient content
        let createContainer = document.createElement("div");
        createContainer.className = "step-ingredient-spacing";
        let createH6 = document.createElement("h3");
        createH6.classList = "reduce-h6";
        let validationDiv = document.createElement("div");
        validationDiv.classList = "invalid-form form-is-valid make-invis";
        let val1P = document.createElement("p");
        val1P.textContent = "Must be between 3 and 400 characters";
        val1P.classList = "make-invis remove-p-margin";
        let val2P = document.createElement("p");
        val2P.textContent = "";
        val2P.classList = "make-invis remove-p-margin";
        let val3P = document.createElement("p");
        val3P.textContent = "Can only contain a-z, A-Z, 0-9, and !@#%&*_+-=?.'/" + '",';
        val3P.classList = "make-invis remove-p-margin";
        let createInput = document.createElement(inputOrTextarea);
        createInput.className = "formValidation recipeGeneralValidation"; //col-10
        createInput.id = arrayClass + arrayIngredientLength;
        createInput.name = arrayClass + arrayIngredientLength;
        // Adds extra classes if textarea
        if(inputOrTextarea == "textarea"){
            createH6.textContent =  "Step " + arrayIngredientLength;
            createInput.rows = "3";
            createInput.cols = "20";
        } else {
            createInput.type = "text";
            createH6.textContent = "Ingredient " + arrayIngredientLength;
        }

        // Creates inital box
        addRemoveLocation.appendChild(createContainer);
        // Creates Variable for insert location and inserts complete box structure
        let innerDivLoc = addRemoveLocation.getElementsByTagName("div").length;
        addRemoveLocation.getElementsByTagName("div")[innerDivLoc-1].appendChild(createH6);
        addRemoveLocation.getElementsByTagName("div")[innerDivLoc-1].appendChild(createInput);
        addRemoveLocation.getElementsByTagName("div")[innerDivLoc-1].appendChild(validationDiv);
        addRemoveLocation.getElementsByTagName("div")[innerDivLoc].appendChild(val1P);
        addRemoveLocation.getElementsByTagName("div")[innerDivLoc].appendChild(val2P);
        addRemoveLocation.getElementsByTagName("div")[innerDivLoc].appendChild(val3P);
        // Adds Validation to newly created container
        addValidation(addRemoveLocation.getElementsByTagName("div")[innerDivLoc-1].getElementsByTagName(inputOrTextarea)[0], "recipeGeneral");
    });

    // Removes last box in list and updates total box count when remove button is clicked
    document.querySelector(removeButton).addEventListener("click", function() {
        // Defensive, forces users to keep a single box on page
        if (arrayIngredientLength > 1){
            let  childTotal = addRemoveLocation.children.length;
            addRemoveLocation.children[childTotal-1].remove();
            // Updates box count variable and counters
            arrayIngredientLength--;
            updateBoxCounters();
        }
    });
}

//Creates functionality for ingredient add/remove buttons
createRemoveFormBoxes("addRemoveLocation ", "dishNumber", "addDish", "ingredients-", ".addDish", "input", "dishTotal" ,".countIngredients");
//Creates functionality for step add/remove buttons
// createRemoveFormBoxes("removeDish", "stepNumber", ".stepAddButton", "steps-", ".stepRemoveButton", "textarea", "stepsTotal", ".countSteps");
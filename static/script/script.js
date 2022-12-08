const tabs = {
  posts: "posts",
  rates: "rates",
};

const buttonStateClass = {
  active: "button-bottom",
  deactive: "button-bottom-deactive",
};

const tabComponents = {
  posts: "postComponent",
  rates: "rateComponent",
};

const tabComponentStateClass = {
  active: "bottom-tab-component-active",
  deactive: "bottom-tab-component-deactive",
};

function useEffect() {
  document.getElementById(tabs.posts).className = buttonStateClass.active;
  document.getElementById(tabs.rates).className = buttonStateClass.deactive;

  document.getElementById(tabComponents.posts).className =
    tabComponentStateClass.active;
  document.getElementById(tabComponents.rates).className =
    tabComponentStateClass.deactive;
}

function setBottomTab(evt) {
  const curDocument = evt.currentTarget;
  if (curDocument.id === tabs.posts) {
    document.getElementById(tabs.posts).className = buttonStateClass.active;
    document.getElementById(tabs.rates).className = buttonStateClass.deactive;

    document.getElementById(tabComponents.posts).className =
      tabComponentStateClass.active;
    document.getElementById(tabComponents.rates).className =
      tabComponentStateClass.deactive;
  } else {
    document.getElementById(tabs.posts).className = buttonStateClass.deactive;
    document.getElementById(tabs.rates).className = buttonStateClass.active;

    document.getElementById(tabComponents.posts).className =
      tabComponentStateClass.deactive;
    document.getElementById(tabComponents.rates).className =
      tabComponentStateClass.active;
  }
}

useEffect();

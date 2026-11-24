// --------------------------------------------------------
// XmlInjector_v4
// --------------------------------------------------------
// --------------------------------------------------------
// This tool is currently being maintained by Triplis.
// Updates are published on the Scumbumbo tribute website.
// --------------------------------------------------------

v4: Added injector for PurchasePickerInteraction, with the ability to inject to categories and purchase_list_options (see Examples folder for examples of how to do these injections).


v3: With the university patch came a change to how computers function, such that access to computers can be locked to specific sims and most of their interactions are what I call "lock aware," meaning they are only usable by sims who have access to the computer. The alternative being interactions that appear on the computer, regardless of locks.

This update to Xml Injector does the following:

- If you are a modder and want interactions you add to the computer to be "lock aware," use the "add_lock_aware_interactions_to_lockable_objects" tuning, along with a list of "super_affordances" (as opposed to "_super_affordances" - the underscore is different for "lock aware" interactions). Apart from that the structure of the tuning is identical to what you would use in the past when adding an interaction to the computer by using "add_interactions_to_objects". The "Examples" folder contains a sample XML file with this tuning used for reference.

- The 'test' interaction that appears on the computer should show up again. It was previously tied to an interaction that was moved to the "lock aware" interactions and thus wasn't triggering from the expected place.

- Reward Traits can be injected using the new add_satisfaction_store_rewards tuning. See the "Examples" folder for a demonstration of how to use it.

Credits: Scumbumbo for the original tool and all of its features. Basemental and alphabetsmells for some help with the code for this update.
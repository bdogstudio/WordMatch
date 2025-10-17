#!/bin/bash

# Word Match - Xcode Project Setup Script
# Run this on macOS to generate a fresh Xcode project

set -e

echo "🎮 Setting up Word Match Xcode Project..."

# Check if we're on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ Error: This script must be run on macOS"
    exit 1
fi

# Check if Xcode is installed
if ! command -v xcodebuild &> /dev/null; then
    echo "❌ Error: Xcode is not installed"
    echo "Please install Xcode from the App Store"
    exit 1
fi

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "📁 Current directory: $SCRIPT_DIR"

# Remove any existing Xcode project (if damaged)
if [ -d "AdjectiveGame.xcodeproj" ]; then
    echo "🗑️  Removing existing Xcode project..."
    rm -rf AdjectiveGame.xcodeproj
fi

# Create the Xcode project directory structure
echo "📦 Creating Xcode project structure..."
mkdir -p AdjectiveGame.xcodeproj/xcshareddata/xcschemes

# Generate a proper project.pbxproj with valid UUIDs
cat > AdjectiveGame.xcodeproj/project.pbxproj << 'PBXPROJ'
// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 56;
	objects = {

/* Begin PBXBuildFile section */
		E7A1B2C34D5F6789012345AB /* AdjectiveGameApp.swift in Sources */ = {isa = PBXBuildFile; fileRef = E7A1B2C34D5F6789012345AA /* AdjectiveGameApp.swift */; };
		E7A1B2C34D5F6789012345AD /* ContentView.swift in Sources */ = {isa = PBXBuildFile; fileRef = E7A1B2C34D5F6789012345AC /* ContentView.swift */; };
		E7A1B2C34D5F6789012345AF /* GameData.swift in Sources */ = {isa = PBXBuildFile; fileRef = E7A1B2C34D5F6789012345AE /* GameData.swift */; };
		E7A1B2C34D5F6789012345B1 /* SetupView.swift in Sources */ = {isa = PBXBuildFile; fileRef = E7A1B2C34D5F6789012345B0 /* SetupView.swift */; };
		E7A1B2C34D5F6789012345B3 /* GameView.swift in Sources */ = {isa = PBXBuildFile; fileRef = E7A1B2C34D5F6789012345B2 /* GameView.swift */; };
		E7A1B2C34D5F6789012345B5 /* ResultsView.swift in Sources */ = {isa = PBXBuildFile; fileRef = E7A1B2C34D5F6789012345B4 /* ResultsView.swift */; };
		E7A1B2C34D5F6789012345B7 /* Assets.xcassets in Resources */ = {isa = PBXBuildFile; fileRef = E7A1B2C34D5F6789012345B6 /* Assets.xcassets */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		E7A1B2C34D5F6789012345A7 /* AdjectiveGame.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = AdjectiveGame.app; sourceTree = BUILT_PRODUCTS_DIR; };
		E7A1B2C34D5F6789012345AA /* AdjectiveGameApp.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AdjectiveGameApp.swift; sourceTree = "<group>"; };
		E7A1B2C34D5F6789012345AC /* ContentView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ContentView.swift; sourceTree = "<group>"; };
		E7A1B2C34D5F6789012345AE /* GameData.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = GameData.swift; sourceTree = "<group>"; };
		E7A1B2C34D5F6789012345B0 /* SetupView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SetupView.swift; sourceTree = "<group>"; };
		E7A1B2C34D5F6789012345B2 /* GameView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = GameView.swift; sourceTree = "<group>"; };
		E7A1B2C34D5F6789012345B4 /* ResultsView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ResultsView.swift; sourceTree = "<group>"; };
		E7A1B2C34D5F6789012345B6 /* Assets.xcassets */ = {isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets; sourceTree = "<group>"; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		E7A1B2C34D5F6789012345A4 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		E7A1B2C34D5F678901234599 = {
			isa = PBXGroup;
			children = (
				E7A1B2C34D5F6789012345A9 /* AdjectiveGame */,
				E7A1B2C34D5F6789012345A8 /* Products */,
			);
			sourceTree = "<group>";
		};
		E7A1B2C34D5F6789012345A8 /* Products */ = {
			isa = PBXGroup;
			children = (
				E7A1B2C34D5F6789012345A7 /* AdjectiveGame.app */,
			);
			name = Products;
			sourceTree = "<group>";
		};
		E7A1B2C34D5F6789012345A9 /* AdjectiveGame */ = {
			isa = PBXGroup;
			children = (
				E7A1B2C34D5F6789012345AA /* AdjectiveGameApp.swift */,
				E7A1B2C34D5F6789012345AC /* ContentView.swift */,
				E7A1B2C34D5F6789012345AE /* GameData.swift */,
				E7A1B2C34D5F6789012345B0 /* SetupView.swift */,
				E7A1B2C34D5F6789012345B2 /* GameView.swift */,
				E7A1B2C34D5F6789012345B4 /* ResultsView.swift */,
				E7A1B2C34D5F6789012345B6 /* Assets.xcassets */,
			);
			path = AdjectiveGame;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		E7A1B2C34D5F6789012345A6 /* AdjectiveGame */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = E7A1B2C34D5F6789012345BA /* Build configuration list for PBXNativeTarget "AdjectiveGame" */;
			buildPhases = (
				E7A1B2C34D5F6789012345A3 /* Sources */,
				E7A1B2C34D5F6789012345A4 /* Frameworks */,
				E7A1B2C34D5F6789012345A5 /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = AdjectiveGame;
			productName = AdjectiveGame;
			productReference = E7A1B2C34D5F6789012345A7 /* AdjectiveGame.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		E7A1B2C34D5F678901234599 /* Project object */ = {
			isa = PBXProject;
			attributes = {
				BuildIndependentTargetsInParallel = 1;
				LastSwiftUpdateCheck = 1500;
				LastUpgradeCheck = 1500;
				TargetAttributes = {
					E7A1B2C34D5F6789012345A6 = {
						CreatedOnToolsVersion = 15.0;
					};
				};
			};
			buildConfigurationList = E7A1B2C34D5F678901234599 /* Build configuration list for PBXProject "AdjectiveGame" */;
			compatibilityVersion = "Xcode 14.0";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = E7A1B2C34D5F678901234599;
			productRefGroup = E7A1B2C34D5F6789012345A8 /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				E7A1B2C34D5F6789012345A6 /* AdjectiveGame */,
			);
		};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		E7A1B2C34D5F6789012345A5 /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				E7A1B2C34D5F6789012345B7 /* Assets.xcassets in Resources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		E7A1B2C34D5F6789012345A3 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				E7A1B2C34D5F6789012345AB /* AdjectiveGameApp.swift in Sources */,
				E7A1B2C34D5F6789012345AD /* ContentView.swift in Sources */,
				E7A1B2C34D5F6789012345AF /* GameData.swift in Sources */,
				E7A1B2C34D5F6789012345B1 /* SetupView.swift in Sources */,
				E7A1B2C34D5F6789012345B3 /* GameView.swift in Sources */,
				E7A1B2C34D5F6789012345B5 /* ResultsView.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		E7A1B2C34D5F6789012345B8 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = YES;
				GCC_C_LANGUAGE_STANDARD = gnu17;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 16.0;
				LOCALIZATION_PREFERS_STRING_CATALOGS = YES;
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				MTL_FAST_MATH = YES;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = iphoneos;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = "DEBUG $(inherited)";
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
			};
			name = Debug;
		};
		E7A1B2C34D5F6789012345B9 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = YES;
				GCC_C_LANGUAGE_STANDARD = gnu17;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 16.0;
				LOCALIZATION_PREFERS_STRING_CATALOGS = YES;
				MTL_ENABLE_DEBUG_INFO = NO;
				MTL_FAST_MATH = YES;
				SDKROOT = iphoneos;
				SWIFT_COMPILATION_MODE = wholemodule;
				VALIDATE_PRODUCT = YES;
			};
			name = Release;
		};
		E7A1B2C34D5F6789012345BB /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_TEAM = "";
				ENABLE_PREVIEWS = YES;
				GENERATE_INFOPLIST_FILE = YES;
				INFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;
				INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;
				INFOPLIST_KEY_UILaunchScreen_Generation = YES;
				INFOPLIST_KEY_UISupportedInterfaceOrientations = UIInterfaceOrientationPortrait;
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown";
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.wordmatch.AdjectiveGame;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Debug;
		};
		E7A1B2C34D5F6789012345BC /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_TEAM = "";
				ENABLE_PREVIEWS = YES;
				GENERATE_INFOPLIST_FILE = YES;
				INFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;
				INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;
				INFOPLIST_KEY_UILaunchScreen_Generation = YES;
				INFOPLIST_KEY_UISupportedInterfaceOrientations = UIInterfaceOrientationPortrait;
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown";
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.wordmatch.AdjectiveGame;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		E7A1B2C34D5F678901234599 /* Build configuration list for PBXProject "AdjectiveGame" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				E7A1B2C34D5F6789012345B8 /* Debug */,
				E7A1B2C34D5F6789012345B9 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		E7A1B2C34D5F6789012345BA /* Build configuration list for PBXNativeTarget "AdjectiveGame" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				E7A1B2C34D5F6789012345BB /* Debug */,
				E7A1B2C34D5F6789012345BC /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */
	};
	rootObject = E7A1B2C34D5F678901234599 /* Project object */;
}
PBXPROJ

# Create the scheme file
cat > AdjectiveGame.xcodeproj/xcshareddata/xcschemes/AdjectiveGame.xcscheme << 'SCHEME'
<?xml version="1.0" encoding="UTF-8"?>
<Scheme
   LastUpgradeVersion = "1500"
   version = "1.7">
   <BuildAction
      parallelizeBuildables = "YES"
      buildImplicitDependencies = "YES">
      <BuildActionEntries>
         <BuildActionEntry
            buildForTesting = "YES"
            buildForRunning = "YES"
            buildForProfiling = "YES"
            buildForArchiving = "YES"
            buildForAnalyzing = "YES">
            <BuildableReference
               BuildableIdentifier = "primary"
               BlueprintIdentifier = "E7A1B2C34D5F6789012345A6"
               BuildableName = "AdjectiveGame.app"
               BlueprintName = "AdjectiveGame"
               ReferencedContainer = "container:AdjectiveGame.xcodeproj">
            </BuildableReference>
         </BuildActionEntry>
      </BuildActionEntries>
   </BuildAction>
   <TestAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      shouldUseLaunchSchemeArgsEnv = "YES"
      shouldAutocreateTestPlan = "YES">
   </TestAction>
   <LaunchAction
      buildConfiguration = "Debug"
      selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB"
      selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB"
      launchStyle = "0"
      useCustomWorkingDirectory = "NO"
      ignoresPersistentStateOnLaunch = "NO"
      debugDocumentVersioning = "YES"
      debugServiceExtension = "internal"
      allowLocationSimulation = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "E7A1B2C34D5F6789012345A6"
            BuildableName = "AdjectiveGame.app"
            BlueprintName = "AdjectiveGame"
            ReferencedContainer = "container:AdjectiveGame.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </LaunchAction>
   <ProfileAction
      buildConfiguration = "Release"
      shouldUseLaunchSchemeArgsEnv = "YES"
      savedToolIdentifier = ""
      useCustomWorkingDirectory = "NO"
      debugDocumentVersioning = "YES">
      <BuildableProductRunnable
         runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "E7A1B2C34D5F6789012345A6"
            BuildableName = "AdjectiveGame.app"
            BlueprintName = "AdjectiveGame"
            ReferencedContainer = "container:AdjectiveGame.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </ProfileAction>
   <AnalyzeAction
      buildConfiguration = "Debug">
   </AnalyzeAction>
   <ArchiveAction
      buildConfiguration = "Release"
      revealArchiveInOrganizer = "YES">
   </ArchiveAction>
</Scheme>
SCHEME

# Set proper permissions
chmod 644 AdjectiveGame.xcodeproj/project.pbxproj
chmod 644 AdjectiveGame.xcodeproj/xcshareddata/xcschemes/AdjectiveGame.xcscheme

# Clear any quarantine attributes
xattr -cr AdjectiveGame.xcodeproj 2>/dev/null || true

echo "✅ Xcode project created successfully!"
echo ""
echo "📱 Next steps:"
echo "   1. Open AdjectiveGame.xcodeproj in Xcode"
echo "   2. Select your target device/simulator"
echo "   3. Press ⌘R to build and run"
echo ""
echo "🎮 Happy coding!"

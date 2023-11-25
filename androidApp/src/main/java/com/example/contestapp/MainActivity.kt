package com.example.contestapp

import ContestAppTheme
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.runtime.LaunchedEffect
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.contestapp.navigation.screen.Screen
import com.example.contestapp.screen.add_lecture_screen.AddLectureScreen
import com.example.contestapp.screen.add_lecture_screen.AddLectureViewModel
import com.example.contestapp.screen.lectures_screen.LecturesScreen
import com.example.contestapp.screen.lectures_screen.LecturesViewModel
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class MainActivity : ComponentActivity() {

    private val viewmodel: MainActivityViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)


        setContent {

            val context = this

            LaunchedEffect(Unit){
                viewmodel.initKoin(context)
            }

            val navController = rememberNavController()

            ContestAppTheme{
                NavHost(navController = navController, startDestination = Screen.LecturesScreen.route){
                    composable(Screen.LecturesScreen.route){
                        val viewModel: LecturesViewModel = hiltViewModel()
                        LecturesScreen(navController = navController, viewModel = viewModel)
                    }
                    composable(Screen.AddLectureScreen.route){
                        val viewModel:AddLectureViewModel = hiltViewModel()
                        AddLectureScreen(navController = navController, viewModel = viewModel)
                    }
                }
            }


        }
    }
}



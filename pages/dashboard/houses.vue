<template>
    <div>
        <h1 class="text-xl font-semibold text-gray-900 sm:text-2xl dark:text-white">Houses</h1>
        <div class="sm:flex mb-4">
            <div class="items-center hidden mb-3 sm:flex sm:divide-x sm:divide-gray-100 sm:mb-0 dark:divide-gray-700">
                <form class="lg:pr-3" action="#" method="GET">
                    <label for="users-search" class="sr-only">Search</label>
                    <div class="relative mt-1 lg:w-64 xl:w-96">
                        <input type="text" name="email" id="users-search"
                            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Search houses">
                    </div>
                </form>
            </div>
            <div class="flex items-center ml-auto space-x-2 sm:space-x-3">
                <Button type="button" data-modal-target="add-user-modal" data-modal-toggle="add-user-modal"
                    class="py-2 bg-blue-800">
                    <svg class="w-5 h-5 mr-2 -ml-1" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"
                            clip-rule="evenodd"></path>
                    </svg>
                    Send Messages
                </Button>
            </div>
        </div>

        <div class="flex flex-row gap-0 mb-5 flex-wrap ">
            <Card class="w-1/6">
                <AspectRatio :ratio="16 / 9" class="bg-muted">
                    <img src="https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800&dpr=2&q=80"
                        alt="Photo by Drew Beamer" class="rounded-md object-cover w-full h-full">
                </AspectRatio>
                <CardContent class="px-2">
                    <div>
                        <h2 class="text-sm font-semibold mt-2">Fully furnished 3 bedroom duplex in Utako Estate.</h2>
                    </div>
                    
                    <div class="flex flex-row gap-5 mt-4 items-center justify-between ">
                        <div>
                            <h1 class="text-base font-semibold text-gray-900 dark:text-white">N 7,000</h1>
                        </div>
                        <Button type="button" data-modal-target="add-user-modal" data-modal-toggle="add-user-modal"
                            class="py-1 bg-lime-700 text-xs ">
                            View
                        </Button>
                    </div>
                    

                </CardContent>
            </Card>
            <Card class="w-1/6">
                <AspectRatio :ratio="16 / 9" class="bg-muted">
                    <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        alt="Photo by Drew Beamer" class="rounded-md object-cover w-full h-full">
                </AspectRatio>
                <CardContent class="px-2">
                    <div>
                        <h2 class="text-sm font-semibold mt-2">Fully furnished 3 bedroom duplex in Utako Estate.</h2>
                    </div>
                    
                    <div class="flex flex-row gap-5 mt-4 items-center justify-between ">
                        <div>
                            <h1 class="text-base font-semibold text-gray-900 dark:text-white">N 7,000</h1>
                        </div>
                        <Button type="button" data-modal-target="add-user-modal" data-modal-toggle="add-user-modal"
                            class="py-1 bg-lime-700 text-xs ">
                            View
                        </Button>
                    </div>

                </CardContent>
            </Card>
            <Card class="w-1/6">
                <AspectRatio :ratio="16 / 9" class="bg-muted">
                    <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        alt="Photo by Drew Beamer" class="rounded-md object-cover w-full h-full">
                </AspectRatio>
                <CardContent class="px-2">
                    <div>
                        <h2 class="text-sm font-semibold mt-2">Fully furnished 3 bedroom duplex in Utako Estate.</h2>
                    </div>
                    
                    <div class="flex flex-row gap-5 mt-4 items-center justify-between ">
                        <div>
                            <h1 class="text-base font-semibold text-gray-900 dark:text-white">N 7,000</h1>
                        </div>
                        <Button type="button" data-modal-target="add-user-modal" data-modal-toggle="add-user-modal"
                            class="py-1 bg-lime-700 text-xs ">
                            View
                        </Button>
                    </div>

                </CardContent>
            </Card>
            <Card class="w-1/6">
                <AspectRatio :ratio="16 / 9" class="bg-muted">
                    <img src="https://images.unsplash.com/photo-1516156008625-3a9d6067fab5?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        alt="Photo by Drew Beamer" class="rounded-md object-cover w-full h-full">
                </AspectRatio>
                <CardContent class="px-2">
                    <div>
                        <h2 class="text-sm font-semibold mt-2">Fully furnished 3 bedroom duplex in Utako Estate.</h2>
                    </div>
                    
                    <div class="flex flex-row gap-5 mt-4 items-center justify-between">
                        <div>
                            <h1 class="text-base font-semibold text-gray-900 dark:text-white">N 7,000</h1>
                        </div>
                        <Button type="button" data-modal-target="add-user-modal" data-modal-toggle="add-user-modal"
                            class="py-1 bg-lime-700 text-xs ">
                            View
                        </Button>
                    </div>

                </CardContent>
            </Card>

            <Card class="w-1/6">
                <AspectRatio :ratio="16 / 9" class="bg-muted">
                    <img src="https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?q=80&w=3184&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        alt="Photo by Drew Beamer" class="rounded-md object-cover w-full h-full">
                </AspectRatio>
                <CardContent class="px-2">
                    <div>
                        <h2 class="text-sm font-semibold mt-2">Fully furnished 3 bedroom duplex in Utako Estate.</h2>
                    </div>
                    
                    <div class="flex flex-row gap-5 mt-4 items-center justify-between">
                        <div>
                            <h1 class="text-base font-semibold text-gray-900 dark:text-white">N 7,000</h1>
                        </div>
                        <Button type="button" data-modal-target="add-user-modal" data-modal-toggle="add-user-modal"
                            class="py-1 bg-lime-700 text-xs ">
                            View
                        </Button>
                    </div>

                </CardContent>
            </Card>

            <Card class="w-1/6">
                <AspectRatio :ratio="16 / 9" class="bg-muted">
                    <img src="https://images.unsplash.com/photo-1516156008625-3a9d6067fab5?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                        alt="Photo by Drew Beamer" class="rounded-md object-cover w-full h-full">
                </AspectRatio>
                <CardContent class="px-2">
                    <div>
                        <h2 class="text-sm font-semibold mt-2">Fully furnished 3 bedroom duplex in Utako Estate.</h2>
                    </div>
                    
                    <div class="flex flex-row gap-5 mt-4 items-center justify-between">
                        <div>
                            <h1 class="text-base font-semibold text-gray-900 dark:text-white">N 7,000</h1>
                        </div>
                        <Button type="button" data-modal-target="add-user-modal" data-modal-toggle="add-user-modal"
                            class="py-1 bg-lime-700 text-xs ">
                            View
                        </Button>
                    </div>

                </CardContent>
            </Card>
            
        </div>
    </div>

</template>

<script setup>
import { AspectRatio } from '@/components/ui/aspect-ratio';
import { Button } from '@/components/ui/button';
definePageMeta({
    layout: 'dashboard'
})
</script>